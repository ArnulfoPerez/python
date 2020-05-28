# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:10:23 2017

@author: arnulfo
"""

import re

l = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

for i in l:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
    print(res.group(3) + " " + res.group(2) + " " + res.group(1))
    
s = "Sun Oct 14 13:47:03 CEST 2012"
expr = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)\b"
x = re.search(expr,s)
print(x.group('hours'))
print(x.group('minutes'))
print(x.start('minutes'))
print(x.end('minutes'))
print(x.span('seconds'))