# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:09:14 2017

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
    if aStr:
        if (char < aStr[0]) or (char > aStr[-1]):
            return False
        low = 0
        high = len(aStr)-1
        if aStr[high]  == char:
            return True
        media = numpy.right_shift(low+high, 1)  
        test = aStr[media]
        if test == char:
            return True
        elif low == high:
            return False
        elif test < char:
            return isIn(char,aStr[media+1:high])
        else:
             return isIn(char,aStr[1:media])
    else:
        return False