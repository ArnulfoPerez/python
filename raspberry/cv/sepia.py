# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 00:18:29 2019

@author: arnulfo
"""
from PIL import Image

def norm(value):
    return min(255,int(value))

def filter (old_red,old_green,old_blue):
    nr = norm((0.393 * old_red) + (0.769 * old_green) + (0.189 * old_blue))
    ng = norm((0.349 * old_red) + (0.686 * old_green) + (0.168 * old_blue))
    nb = norm((0.272 * old_red) + (0.534 * old_green) + (0.131 * old_blue))
    return (nr,ng,nb)

im = Image.open('image.png') 
rgb_im = im.convert('RGB')
width, height = im.size
out = Image.new('RGB', (width, height))
for row in range(height): 
    for col in range(width):
        r, g, b = rgb_im.getpixel((col, row)) 
        out.putpixel((col, row), filter (r,g,b))
out.save("sepia.png")