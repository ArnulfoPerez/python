# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:13:27 2017

@author: Arnulfo
"""

import timeit
# OR just import it in the local namespace
from costly import costly_function
print(timeit.timeit(costly_function, number=1000))

def costly_func():
    return map(lambda x: x^2, range(10))
def costly_funca(lst):
    return map(lambda x: x^2, lst)
#You could measure it using a decorator defined like this:

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

short_list = range(10) 
wrapped = wrapper(costly_funca, short_list)
print(timeit.timeit(wrapped, number=1000))
long_list = range(1000)
wrapped = wrapper(costly_funca, long_list)
print(timeit.timeit(wrapped, number=1000))

# Measure it since costly_func is a callable without argument
print(timeit.timeit(costly_func))
# Measure it using raw statements
print(timeit.timeit('map(lambda x: x^2, range(10))'))

print(timeit.timeit('costly_function()', setup='from costly import costly_function', number=1000))
