# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 12:45:37 2017

@author: Arnulfo
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    maxKeyLength = 0
    for key in aDict.keys():
      length = len(aDict[key])
      if length > maxKeyLength:
          maxKey = key
          maxKeyLength = length
    return maxKey