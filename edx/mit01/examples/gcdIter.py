# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:56:05 2017

@author: Arnulfo
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b > a:
        r2 = b
        r1 = a
    else:
        r2 = a
        r1 = b
    while True:
        r0 = r2  - r1 * (r2//r1)
        if r0 == 0:
            break
        else:
            r2 = r1
            r1 = r0
    return r1
        