# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:13:23 2019

@author: arnulfo
"""
number = 1867
prime = True

for i in range(number-2):
    if not (number % (i+2)):
        prime = False

print( "not "*(not prime) +"prime")