# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:43:07 2017

@author: Arnulfo Pérez

A regular polygon has 'n' number of sides. Each side has length 's'.

* The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
* The perimeter of a polygon is: length of the boundary of the polygon

'polysum' that takes 2 arguments, 
Input
    n (Int) > 0   number of sides
    s (Float) > 0 length of each side
    
Output
    Sums the area and square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    
"""

def polysum(n,s):
    import math
    area = (0.25 * n * s * s)/math.tan(math.pi/n)
    perimeter = n*s
    return round( area + perimeter*perimeter,4)