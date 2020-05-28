# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:06:59 2019

@author: arnulfo
"""

from turtle import Turtle
from random import randint



laura = Turtle()
rik = Turtle()
lauren = Turtle()
carrieanne = Turtle()

colors = ['red','purple','green','blue']
index = 0

turtles = [laura,rik,lauren,carrieanne]
startx, starty = -160, 100
for t in turtles:
    t.color(colors[index])
    t.shape('turtle')
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    starty += 40
    index += 1

for movement in range(100):
    for t in turtles:
        t.forward(randint(1,5))
        
input("Press Enter to close")

exit()


