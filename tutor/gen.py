# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:46:25 2017

@author: arnulfo
"""

def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i

def gen2():
    yield from "Python"
    yield from range(5)

g1 = gen1()
g2 = gen2()
print("g1: ", end=", ")
for x in g1:
    print(x, end=", ")
print("\ng2: ", end=", ")
for x in g2:
    print(x, end=", ")
print()

def subgenerator():
    yield 1
    return 42

def delegating_generator():
    x = yield from subgenerator()
    print(x)

for x in delegating_generator():
    print(x)

def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc

for p in permutations(['r','e','d']): print(''.join(p))
for p in permutations(list("game")): print(''.join(p) + ", ", end="")