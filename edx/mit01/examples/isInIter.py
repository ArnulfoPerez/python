# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:54:08 2017

@author: Arnulfo
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    import numpy  
    if (char < aStr[0]) or (char > aStr[-1]):
        return False
    low = 0
    high = len(aStr)-1
    while(low<high):
        media = numpy.right_shift(low+high, 1)  
        test = aStr[media]
        if test == char:
            return True
        elif test < char:
            low = media
        else:
            high = media
    return False
    