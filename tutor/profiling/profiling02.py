import time                                                

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts))
        return result

    return timed
# You can use the timeit function like this:

@timeit
def longRunningOperation(dummyArg, optionalDummyArg=None):
    time.sleep(3)
    
longRunningOperation("test", "optional test")