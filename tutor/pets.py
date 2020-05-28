# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:41:41 2017

@author: Arnulfo
"""

class Pets:
    name = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))
    
class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"

class Cats(Pets):
    name = "cats"

p = Pets()
p.about()

d = Dogs()
d.about()

c = Cats()
c.about()