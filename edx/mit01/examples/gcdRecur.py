# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:27:01 2017

@author: Arnulfo
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)