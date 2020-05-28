# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:02:58 2017

@author: Arnulfo
"""
# Planck constant
h = 6.626e-34
# speed of light
c = 2.998e8
def up(l):
    return (4e15/3)*l*l*l - 0.6e9*l*l
def down(l):
    return (5.2e9/2)*l*l -(4e15/3)*l*l*l
def irr():
    return (1/(h*c))*(up(800e-9)-up(300e-9)+down(1300e-9)-down(800e-9))

print(irr())