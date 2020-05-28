# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:34:22 2017

@author: Arnulfo
"""
x='x'
print(x, end=" ")  # Appends a space instead of a newline
print(x, end=" ")  # Appends a space instead of a newline
print(x, end=" ")  # Appends a space instead of a newline

x = b"Hallo"
t = str(x)
u = t.encode("UTF-8")
print(u)
assert int(hex(65),0) == int(0x41)

x = ["a","b","c"]
y = [x] * 4
assert y == [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
y[0][0] = "p"
print(y)