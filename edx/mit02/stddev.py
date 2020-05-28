# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:41:28 2017

@author: arnulfo
"""
import statistics
import math

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L:
        return statistics.pstdev([len(s) for s in L])
    else:
        return math.nan