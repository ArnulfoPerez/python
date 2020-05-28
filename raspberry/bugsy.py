# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 00:24:55 2019

@author: arnulfo
"""

names = ['Alice', 'Bob', 'Carol', 'Dan', 'Eve']
ages = [22, 32, 18, 57, 41]
current_year = 2017

for person in range(len(names)):
    age = ages[person]
    name = names[person]
    year_of_birth = current_year - age
    print(name + ' was born in ' + str(year_of_birth))

