# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:25:59 2017

@author: arnulfo
"""

class C: 
    counter = 0
    def __init__(self): 
        type(self).counter += 1
    def __del__(self):
        type(self).counter -= 1
        
class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @staticmethod
    def RobotInstances():
        return Robot.__counter
               

if __name__ == "__main__":
    x = C()
    print("Number of instances: : {:0}".format(C.counter))
    y = C()
    print("Number of instances: : {:0}".format(C.counter))
    del x
    print("Number of instances: : {:0}".format(C.counter))
    del y
    print("Number of instances: : {:0}".format(C.counter))
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())  