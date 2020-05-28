# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:59:13 2017

@author: Arnulfo
"""

class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x