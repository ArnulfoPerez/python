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

scale = 50
            
smiley=Image.new("RGB",(scale*10,scale*10))
width, height = smiley.size

for row in range(height):
	for col in range(width):
		smiley.putpixel((col,row),face[int(row/scale)][int(col/scale)])
smiley.save('smiley_scaled.jpg')