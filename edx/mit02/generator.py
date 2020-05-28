# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 00:47:16 2017

@author: arnulfo
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        combo2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
            else:
                combo2.append(items[j])
        for x in powerSet(combo2):
            yield (combo,x)
            
for l in yieldAllCombos([1,2,3]):
    print(l)