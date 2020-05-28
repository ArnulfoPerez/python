# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:04:08 2019

@author: arnulfo
"""

print("\n".join(["Fizz" * (i % 3 == 0) + "Buzz" *(i % 5 == 0) or str(i) for i in range(1, 100)]))

