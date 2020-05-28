# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 02:47:25 2019

@author: arnulfo
"""

#import Image module from PIL library
from PIL import Image

#path to image to hide within here
image = Image.open('image.png')
rgb_image = image.convert('RGB') #convert to RGB

width, height = image.size #assign the image width and height to variables

#message = input("What message do you want to hide?")
message = 'hola mundo'

#I'm going to use the message "hello everybody!" as an example

binary_message = ""

#The for loop will repeat for each character of "hello everybody!", including the space and the exclamation mark

for char in message:
    ascii_number = ord(char) #This converts the ASCII character into the denary number that represents it
                             #For the first letter, 'h', this gives '104'
                             
    bin_as_string = bin(ascii_number) #This converts that denary number into a string representing a binary number
                                      #So '104' is converted into the string '0b1101000'
                                      #The 'b' is added in by 'bin()' to show the number is binary
                                      
    bin_as_string = bin_as_string.replace('b','') #This removes the 'b'
                                                  #So finally you get '01101000'
    
    while len(bin_as_string) < 8 :
        bin_as_string = '0' + bin_as_string #This lengthens the binary number string until it is 8 bits
                                            #Our example is already 8 bits long, so it remains '01101000'

    binary_message = binary_message + bin_as_string #This result is then added to the binary message

#Create a grid for the output image
output_image = Image.new('RGB', (width,height))

#Create a variable to keep track of how far through the binary message the code has got
i = 0

#Set up loops to modify each pixel within the image
for row in range(height):
    for col in range(width):
        r, g, b = rgb_image.getpixel((col, row))

        #Start by converting the red value of the pixel to binary  
        bin_r = bin(r)    
        
        #If the binary message has not been completely encoded, the code does the following things
        if i < len(binary_message):     
             
            
            #Replace the final bit with a 1 or a 0 from the message    
            if binary_message[i] == '1':
                bin_r = bin_r[:-1] + '1'
            else:
                bin_r = bin_r[:-1] + '0'
                
        #Once the message has been completely encoded, the code replaces every red value's last bit with a zero
        #This isn't good steganography, but it's simple to implement
        else:
            bin_r = bin_r[:-1] + '0'
            
        #The binary number for the red value is converted back to an integer
        new_r = int(bin_r,2)
        
        #This integer is set as the pixel's red value
        output_image.putpixel((col, row), (new_r,g,b))
        
        #The variable i is increased by 1 to move on to the next binary character of the message
        i = i + 1

#Once the code has iterated over all pixels in the image to change their red values, the image is saved
output_image.save("encodedx_image.png")

