# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:04:18 2019

@author: arnulfo
"""

from shapes import Triangle, Rectangle, Oval,Paper

# Now, let’s create an instance of a Rectangle object.

rect1 = Rectangle()

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")

#tri = Triangle()

#tri.set_color("green")

#ov = Oval()

#ov.set_width(200)
#ov.set_height(100)
#ov.set_color("red")

# Finally, let’s call another method to draw the Rectangle object we have created:

rect1.draw()
#tri.draw()
#ov.draw()

#input("Press Enter to close")
Paper.display()