import copy
import gc
import pickle
import sys
import unittest
import warnings
import weakref
import inspect
import types

from test import support


class FinalizationTest(unittest.TestCase):

    def test_frame_resurrect(self):
        # A generator frame can be resurrected by a generator's finalization.
        def gen():
            nonlocal frame
            try:
                yield
            finally:
                frame = sys._getframe()

        g = gen()
        wr = weakref.ref(g)
        next(g)
        del g
        support.gc_collect()
        self.assertIs(wr(), None)
        self.assertTrue(frame)
        del frame
        support.gc_collect()

    def test_refcycle(self):
        # A generator caught in a refcycle gets finalized anyway.
        old_garbage = gc.garbage[:]
        finalized = False
        def gen():
            nonlocal finalized
            try:
                g = yield
                yield 1
            finally:
                finalized = True

        g = gen()
        next(g)
        g.send(g)
        self.assertGreater(sys.getrefcount(g), 2)
        self.assertFalse(finalized)
        del g
        support.gc_collect()
        self.assertTrue(finalized)
        self.assertEqual(gc.garbage, old_garbage)

    def test_lambda_generator(self):
        # Issue #23192: Test that a lambda returning a generator behaves
        # like the equivalent function
        f = lambda: (yield 1)
        def g(): return (yield 1)

        # test 'yield from'
        f2 = lambda: (yield from g())
        def g2(): return (yield from g())

        f3 = lambda: (yield from f())
        def g3(): return (yield from f())

        for gen_fun in (f, g, f2, g2, f3, g3):
            gen = gen_fun()
            self.assertEqual(next(gen), 1)
            with self.assertRaises(StopIteration) as cm:
                gen.send(2)
            self.assertEqual(cm.exception.value, 2)


class GeneratorTest(unittest.TestCase):

    def test_name(self):
        def func():
            yield 1

        # check generator names
        gen = func()
        self.assertEqual(gen.__name__, "func")
        self.assertEqual(gen.__qualname__,
                         "GeneratorTest.test_name.<locals>.func")

        # modify generator names
        gen.__name__ = "name"
        gen.__qualname__ = "qualname"
        self.assertEqual(gen.__name__, "name")
        self.assertEqual(gen.__qualname__, "qualname")

        # generator names must be a string and cannot be deleted
        self.assertRaises(TypeError, setattr, gen, '__name__', 123)
        self.assertRaises(TypeError, setattr, gen, '__qualname__', 123)
        self.assertRaises(TypeError, delattr, gen, '__name__')
        self.assertRaises(TypeError, delattr, gen, '__qualname__')

        # modify names of the function creating the generator
        func.__qualname__ = "func_qualname"
        func.__name__ = "func_name"
        gen = func()
        self.assertEqual(gen.__name__, "func_name")
        self.assertEqual(gen.__qualname__, "func_qualname")

        # unnamed generator
        gen = (x for x in range(10))
        self.assertEqual(gen.__name__,
                         "<genexpr>")
        self.assertEqual(gen.__qualname__,
                         "GeneratorTest.test_name.<locals>.<genexpr>")

    def test_copy(self):
        def f():
            yield 1
        g = f()
        with self.assertRaises(TypeError):
            copy.copy(g)

    def test_pickle(self):
        def f():
            yield 1
        g = f()
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.assertRaises((TypeError, pickle.PicklingError)):
                pickle.dumps(g, proto)


class ExceptionTest(unittest.TestCase):
    # Tests for the issue #23353: check that the currently handled exception
    # is correctly saved/restored in PyEval_EvalFrameEx().

    def test_except_throw(self):
        def store_raise_exc_generator():
            try:
                self.assertEqual(sys.exc_info()[0], None)
                yield
            except Exception as exc:
                # exception raised by gen.throw(exc)
                self.assertEqual(sys.exc_info()[0], ValueError)
                self.assertIsNone(exc.__context__)
                yield

                # ensure that the exception is not lost
                self.assertEqual(sys.exc_info()[0], ValueError)
                yield

                # we should be able to raise back the ValueError
                raise

        make = store_raise_exc_generator()
        next(make)

        try:
            raise ValueError()
        except Exception as exc:
            try:
                make.throw(exc)
            except Exception:
                pass

        next(make)
        with self.assertRaises(ValueError) as cm:
            next(make)
        self.assertIsNone(cm.exception.__context__)

        self.assertEqual(sys.exc_info(), (None, None, None))

    def test_except_next(self):
        def gen():
            self.assertEqual(sys.exc_info()[0], ValueError)
            yield "done"

        g = gen()
        try:
            raise ValueError
        except Exception:
            self.assertEqual(next(g), "done")
        self.assertEqual(sys.exc_info(), (None, None, None))

    def test_except_gen_except(self):
        def gen():
            try:
                self.assertEqual(sys.exc_info()[0], None)
                yield
                # we are called from "except ValueError:", TypeError must
                # inherit ValueError in its context
                raise TypeError()
            except TypeError as exc:
                self.assertEqual(sys.exc_info()[0], TypeError)
                self.assertEqual(type(exc.__context__), ValueError)
            # here we are still called from the "except ValueError:"
            self.assertEqual(sys.exc_info()[0], ValueError)
            yield
            self.assertIsNone(sys.exc_info()[0])
            yield "done"

        g = gen()
        next(g)
        try:
            raise ValueError
        except Exception:
            next(g)

        self.assertEqual(next(g), "done")
        self.assertEqual(sys.exc_info(), (None, None, None))

    def test_except_throw_exception_context(self):
        def gen():
            try:
                try:
                    self.assertEqual(sys.exc_info()[0], None)
                    yield
                except ValueError:
                    # we are called from "except ValueError:"
                    self.assertEqual(sys.exc_info()[0], ValueError)
                    raise TypeError()
            except Exception as exc:
                self.assertEqual(sys.exc_info()[0], TypeError)
                self.assertEqual(type(exc.__context__), ValueError)
            # we are still called from "except ValueError:"
            self.assertEqual(sys.exc_info()[0], ValueError)
            yield
            self.assertIsNone(sys.exc_info()[0])
            yield "done"

        g = gen()
        next(g)
        try:
            raise ValueError
        except Exception as exc:
            g.throw(exc)

        self.assertEqual(next(g), "done")
        self.assertEqual(sys.exc_info(), (None, None, None))

    def test_stopiteration_warning(self):
        # See also PEP 479.

        def gen():
            raise StopIteration
            yield

        with self.assertRaises(StopIteration), \
             self.assertWarnsRegex(DeprecationWarning, "StopIteration"):

            next(gen())

        with self.assertRaisesRegex(DeprecationWarning,
                                    "generator .* raised StopIteration"), \
             warnings.catch_warnings():

            warnings.simplefilter('error')
            next(gen())


    def test_tutorial_stopiteration(self):
        # Raise StopIteration" stops the generator too:

        def f():
            yield 1
            raise StopIteration
            yield 2 # never reached

        g = f()
        self.assertEqual(next(g), 1)

        with self.assertWarnsRegex(DeprecationWarning, "StopIteration"):
            with self.assertRaises(StopIteration):
                next(g)

        with self.assertRaises(StopIteration):
            # This time StopIteration isn't raised from the generator's body,
            # hence no warning.
            next(g)

    def test_return_tuple(self):
        def g():
            return (yield 1)

        gen = g()
        self.assertEqual(next(gen), 1)
        with self.assertRaises(StopIteration) as cm:
            gen.send((2,))
        self.assertEqual(cm.exception.value, (2,))

    def test_return_stopiteration(self):
        def g():
            return (yield 1)

        gen = g()
        self.assertEqual(next(gen), 1)
        with self.assertRaises(StopIteration) as cm:
            gen.send(StopIteration(2))
        self.assertIsInstance(cm.exception.value, StopIteration)
        self.assertEqual(cm.exception.value.value, 2)


class YieldFromTests(unittest.TestCase):
    def test_generator_gi_yieldfrom(self):
        def a():
            self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_RUNNING)
            self.assertIsNone(gen_b.gi_yieldfrom)
            yield
            self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_RUNNING)
            self.assertIsNone(gen_b.gi_yieldfrom)

        def b():
            self.assertIsNone(gen_b.gi_yieldfrom)
            yield from a()
            self.assertIsNone(gen_b.gi_yieldfrom)
            yield
            self.assertIsNone(gen_b.gi_yieldfrom)

        gen_b = b()
        self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_CREATED)
        self.assertIsNone(gen_b.gi_yieldfrom)

        gen_b.send(None)
        self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_SUSPENDED)
        self.assertEqual(gen_b.gi_yieldfrom.gi_code.co_name, 'a')

        gen_b.send(None)
        self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_SUSPENDED)
        self.assertIsNone(gen_b.gi_yieldfrom)

        [] = gen_b  # Exhaust generator
        self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_CLOSED)
        self.assertIsNone(gen_b.gi_yieldfrom)


tutorial_tests = """
