# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:46:21 2017

@author: Arnulfo
"""
def mean(first, *args):
    '''
    Calculates the arithmetic mean of a variable number of values.
    '''
    if args == []:
        return first
    return (first + sum([x for x in args]))/(len(args) + 1)

assert mean(1, 2, 3) == 2
