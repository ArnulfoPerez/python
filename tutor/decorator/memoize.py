# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:21:52 2017

@author: Arnulfo
"""
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def timing(func,n):
    time = timeit.timeit(wrapper(func, n), number=1000)
    print('{0:<10s} {1:} secs'.format(func.__name__,time))

n = 20
timing(memoize(fib),n)
timing(fib,n)

