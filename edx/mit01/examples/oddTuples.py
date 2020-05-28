# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:47:22 2017

@author: Arnulfo
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    if len(aTup) > 0:
        acc = ()
        for i in range(0,len(aTup),2):
            acc += ((aTup[i],))
        return acc
    else:
        return ()