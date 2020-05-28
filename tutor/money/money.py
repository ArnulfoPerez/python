# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:12:51 2017

@author: Arnulfo
"""

class Money:

    __exchange = {"Euro" : 1.0, "US Dollar" : 0.930916, "British Pound" : 1.150771,
              "Indian Rupee" : 0.014234,
                "Australian Dollar" : 0.716992, "Canadian Dollar" : 0.697457,
                "Singapore Dollar" : 0.664199,
                "Swiss Franc" : 0.933290 }
    
    def __init__(self, value, unit = "Euro" ):
        self.value = value
        self.unit = unit
    
    def Converse2Euros(self):
        return self.value * Money.__exchange[self.unit]
    
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Euros() + other
        else:
            l = self.Converse2Euros() + other.Converse2Euros()
        return Money(l / Money.__exchange[self.unit], self.unit )

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Euros() + other
        else:
            l = self.Converse2Euros() + other.Converse2Euros()
        self.value = l / Money.__exchange[self.unit]
        return self
    
    def __str__(self):
        return str(self.Converse2Euros())
    
    def __repr__(self):
        return "Money(" + str(self.value) + ", '" + self.unit + "')"
        
    def __radd__(self, other):
        return Money.__add__(self,other)  
    
    

if __name__ == "__main__":
    x = Money(4)
    print(x)
    y = eval(repr(x))

    z = Money(4.5, "US Dollar") + Money(1)
    print(repr(z))
    print(z)