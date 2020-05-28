# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 01:10:57 2017

@author: arnulfo
"""

from itertools import combinations

def powerSet(s): 
        for r in range(len(s)+1):
            for x in combinations(s, r):
                yield list(x)
    
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    s = set(items)
    for x in powerSet(items):  
        for y in powerSet(list(s.difference(set(x)))):
            yield (x,y)

for l in powerSet([1,2,3]):
    print(l)

for l in yieldAllCombos([1,2,3]):
    print(l)
    