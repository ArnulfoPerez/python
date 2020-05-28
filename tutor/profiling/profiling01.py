from profilehooks import profile, coverage, timecall
import time

@profile(immediate=True)    # or @coverage
def fn(n):
    if n < 2: return 1
    else: return n * fn(n-1)
print(fn(42))

@timecall(immediate=True)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(10))

@coverage
def f3(a, *args, **kw):
    time.sleep(0.3)
    print( 'f3', args, kw)
    
f3(1,2,3)