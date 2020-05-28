# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:13:23 2019

@author: arnulfo
"""
from math import sqrt
number = 1867
prime = True

for i in range(int(sqrt(number))):
    if not (number % (i+2)):
        prime = False
        break

print( "not "*(not prime) +"prime")