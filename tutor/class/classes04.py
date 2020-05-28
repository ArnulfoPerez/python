# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:38:30 2017

@author: arnulfo
"""

class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter

class Pets:
    name = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))
    
class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"

class Cats(Pets):
    name = "cats"

class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val    
            
class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber



if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
    
    p = Pets()
    p.about()

    d = Dogs()
    d.about()
    
    c = Cats()
    c.about()
    
    x = OurClass(10)
    print(x.OurAtt) 
    x.OurAtt = 2000
    print(x.OurAtt)
    x = OurClass(-10)
    print(x.OurAtt) 
    
    x = Person("Marge", "Simpson")
    y = Employee("Homer", "Simpson", "1007")
    
    print(x.Name())
    print(y.GetEmployee())