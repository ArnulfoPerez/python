# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:56:55 2019

@author: arnulfo
"""

from PIL import Image

original = Image.open("puppy.bmp")

ori_width, ori_height = original.size
rot_height, rot_width = ori_width, ori_height

rotated = Image.new("RGB", (rot_width, rot_height))

for y in range(ori_height):
    for x in range(ori_width):
        pixel = original.getpixel((x, y))
        rotated.putpixel((rot_width - 1 - y, x), pixel)

rotated.save('rotated_puppy.jpg', 'JPEG')