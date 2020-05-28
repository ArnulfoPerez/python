# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import copy

class CustomClass(object): # Custom class example
    def __init__(self, thing):
        self.thing = thing
        
original = CustomClass("original")
copia = copy.copy(original)
copia.thing = "copia"
print(original.thing)
print(copia.thing)