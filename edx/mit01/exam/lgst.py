# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:16:42 2017

@author: Arnulfo
"""

def longest(order, L):
    """
    return longest sequence with order
    """
    size = len(L)
    longest_sequence = []
    ll = 0
    for i in range(size):
        sequence = [L[i]]
        for j in range(i+1, size):
            if order(L[j-1], L[j]):
                sequence.append(L[j])
            else:
                break
        ls = len(sequence)
        if ls > ll:
            longest_sequence = sequence[:]
            ll = ls
    return longest_sequence
    
print(longest(lambda x, y: not x < y, [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
print(longest(lambda x, y: not x > y, [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
print(longest(lambda x, y: x >= y, [5, 4, 10]))
print(longest(lambda x, y: x <= y, [5, 4, 10]))

