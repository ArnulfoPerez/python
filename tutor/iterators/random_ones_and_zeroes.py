# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:46:02 2017

@author: Arnulfo
"""
from random import random
def random_ones_and_zeroes():
    while True:
        yield 0 if random()< 0.5 else 1

binary_generator = random_ones_and_zeroes()
for i in range(20):
    print(next(binary_generator), end = " ")
print()
    