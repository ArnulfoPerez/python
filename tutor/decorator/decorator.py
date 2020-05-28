# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:15:49 2017

@author: Arnulfo
"""

from functools import wraps

def get_ready(gen):
    """
    Decorator: gets a generator gen ready 
    by advancing to first yield statement
    """
    @wraps(gen)
    def generator(*args,**kwargs):   
        g = gen(*args,**kwargs)   
        next(g)   
        return g   
    return generator

@get_ready
def infinite_looper(objects):
    count = -1
    message = yield None
    while True:
        if message != None:
            count = 0 if message < 0 else message
        count += 1
        if count >= len(objects):
            count = 0
        message = yield objects[count]
            

x = infinite_looper("abcdef") 
#print(next(x))
print(x.send(4))
print(next(x))
print(next(x))
print(x.send(5))
print(next(x))