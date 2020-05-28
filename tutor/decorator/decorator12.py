def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


def foo(x):
    print(42)
print()
print('decorating with two step binding:')
greeting2 = greeting("Καλημέρα")
foo = greeting2(foo)
foo("Hi")
print()
print('decorating with currying:')
foo = greeting("Καλημέρα")(foo)
foo("Hi")