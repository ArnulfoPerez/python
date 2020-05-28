# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 21:43:27 2017

@author: Arnulfo
"""
from copy import deepcopy

lst1 = ['a','b',['ab','ba']]
lst2 = deepcopy(lst1)
assert lst1 == ['a', 'b', ['ab', 'ba']]
assert lst2 == ['a', 'b', ['ab', 'ba']]
assert id(lst1) != id(lst2)
assert id(lst1[0]) == id(lst2[0])
assert id(lst2[2]) != id(lst1[2])

x = 3
y = x
assert id(x) == id(y)
y = 4
assert id(x) != id(y)
assert x == 3

colours1 = ["red", "blue"]
colours2 = colours1

assert id(colours1) == id(colours2)
colours2 = ["rouge", "vert"]
assert id(colours1) != id(colours2)
assert colours1 == ["red", "blue"]

colours2 = colours1
assert id(colours1) == id(colours2)
colours2[1] = "green"
assert id(colours1) == id(colours2)
assert colours1 == ['red', 'green']
assert colours2 == ['red', 'green']

lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[0] = 'c'
assert lst1 == ['a', 'b', ['ab', 'ba']]
assert lst2 == ['c', 'b', ['ab', 'ba']]

lst2[2][1] = 'd'
assert lst1 == ['a', 'b', ['ab', 'd']]
assert lst2 == ['c', 'b', ['ab', 'd']]