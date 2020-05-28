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
for row in range(height): 
    for col in range(width):
        r, g, b = rgb_im.getpixel((col, row)) 
        out.putpixel((col, row), (255 - r, 255 - g, 255 - b))
out.save("negative.png")