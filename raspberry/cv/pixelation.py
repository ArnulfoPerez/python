# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 00:18:29 2019

@author: arnulfo
"""
from PIL import Image

im = Image.open('image.png') 
rgb_im = im.convert('RGB')
width, height = im.size
out = Image.new('RGB', (width, height))
pixelAmount = 8
                            
for row in range(0, height - pixelAmount, pixelAmount):
    for col in range(0, width - pixelAmount, pixelAmount):
        r, g, b = rgb_im.getpixel((col, row))
        for o in range(row, row + pixelAmount):
            for p in range(col, col + pixelAmount):
                out.putpixel((p,o), (r,g,b))
                            
                            
out.save("pixelated.png")