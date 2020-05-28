# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:34:22 2017

@author: Arnulfo
"""
import functools
from math import sin, cos, tan, pi

def celsius2fahrenheit(temperature):
    """
    converts Celsius to Farenheit
    """
    return (float(9)/5)*temperature + 32

T = (36.5, 37, 37.5, 38, 39)
F = list(map(celsius2fahrenheit, T))
C = [celsius2fahrenheit(x) for x in T]
L = [(float(9)/5)*x + 32 for x in T]
print(max(map(lambda x: (9.0/5)*x + 32, T)))
assert F == C
assert C == L
print(F)
print(C)
print(L)

A = [1, 2, 3, 4]
B = [17, 12, 11, 10]
C = [-1, -4, 5, 9]
map(lambda x, y: x+y, A, B)
map(lambda x, y, z: x+y+z, A, B, C)
map(lambda x, y, z: 2.5*x + 2*y - z, A, B, C)

print([func(pi) for func in (sin, cos, tan)])

FIBO = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
print(list(filter(lambda x: x % 2, FIBO)))
print(list(filter(lambda x: x % 2 == 0, FIBO)))

print(functools.reduce(lambda x, y: x + y, [47, 11, 42, 13]))

pairs = [(1,2),(2,3),(3,4)]
for x in map(lambda args:(args[0],2*args[1]),pairs):
    print(x)

