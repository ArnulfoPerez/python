# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:12:16 2019

@author: arnulfo
"""

from PIL import Image

b=(0,0,0)
y=(255,255,0)
face=[[b,b,b,b,y,y,b,b,b,b],
            [b,b,y,y,y,y,y,y,b,b],
            [b,y,y,y,y,y,y,y,y,b],
            [b,y,y,b,y,y,b,y,y,b],
            [y,y,y,y,y,y,y,y,y,y],
            [y,y,b,y,y,y,y,b,y,y],
            [b,y,y,b,b,b,b,y,y,b],
            [b,y,y,y,y,y,y,y,y,b],
            [b,b,y,y,y,y,y,y,b,b],
            [b,b,b,b,y,y,b,b,b,b]]
            
smiley=Image.new("RGB",(10,10))
width, height = smiley.size

for row in range(height):
	for col in range(width):
		smiley.putpixel((col,row),face[row][col])
smiley.save('smiley.jpg')
smiley.show()