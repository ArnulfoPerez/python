# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:07:22 2017

@author: Arnulfo
"""

class C: 

    counter = 0
    
    def __init__(self): 
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))