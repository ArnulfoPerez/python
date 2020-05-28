# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:48:17 2017

@author: Arnulfo
"""

def gen():
    yield 1
    raise StopIteration(42)

def genR():
    yield 1
    return 42

def infinite_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        message = yield objects[count]
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1

def infinite_looperE(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        try:
            message = yield objects[count]
        except Exception:
            print("index: " + str(count))
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1

class StateOfGenerator(Exception):
     def __init__(self, message=None):
         self.message = message

def infinite_looperS(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        try:
            message = yield objects[count]
        except StateOfGenerator:
            print("index: " + str(count))
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1            


def simple_coroutine():
    print("coroutine has been started!")
    x = yield 
    print("coroutine received: ", x)

cr = simple_coroutine()
cr