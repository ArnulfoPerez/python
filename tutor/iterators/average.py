# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:46:59 2017

@author: Arnulfo
"""

from functools import wraps

def get_ready(gen):
    """
    Decorator: gets a generator gen ready
    by advancing to first yield statement
    """
    @wraps(gen)
    def generator(*args, **kwargs):
        '''
        Generator wrapper
        '''
        dummy = gen(*args, **kwargs)
        next(dummy)
        return dummy
    return generator

@get_ready
def running_average(initial_value = 0, weight = 0.5):
    '''
    Returns the running average of a sequence using weight
    '''
    average = initial_value
    while True:
        value = yield average
        average = average * (1-weight) + value * weight
    