# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 02:33:25 2019

@author: arnulfo
"""

#Import Image module from PIL library
from PIL import Image

#Path to image containing message here
image = Image.open('encodedx_image.png')

#Convert to RGB
rgb_image = image.convert('RGB')

#Assign the image width and height to variables
width, height = image.size

i = 0

output_bits = ""
output_text = ""

#Set up loops to address each pixel in the image
for row in range(height):
    for col in range(width):
      r, g, b = rgb_image.getpixel((col, row))
      bin_r = bin(r)
      output_bits += bin_r[-1]

end = False
while end == False:
    byte = int(output_bits[:8],2)
    #print(byte)
    if byte == 0:
        end = True
    else:
        output_text = output_text + chr(byte)
        output_bits = output_bits[8:]

print(output_text)

