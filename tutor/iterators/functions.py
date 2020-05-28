# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:11:07 2017

@author: Arnulfo
"""

def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")

print("The docstring of the function Hello: " + Hello.__doc__)
Hello()

def no_return(x,y):
    pass

print(no_return(4,5))

def empty_return(x,y):
    pass
    return

print(empty_return(4,5))

def fib_intervall(x):
    """ returns the largest fibonacci
    number smaller than x and the lowest
    fibonacci number higher than x"""
    if x < 0:
        return -1
    (old,new, lub) = (0,1,0)
    while True:
        if new < x:
            lub = new 
            (old,new) = (new,old+new)
        else:
            return (lub, new)
            
while True:
    x = int(input("Your number: "))
    if x <= 0:
        break
    (lub, sup) = fib_intervall(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))
    
def f():
    print('inside function')
    global s
    print(s)
    s = "function scope"
    print(s)
s = "global scope" 
f()
print('outside function')
print(s)

def arithmetic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """

    return (first + sum(values)) / (1 + len(values))

print([arithmetic_mean(*x) for *x in [(45,32,89,78),(8989.8,78787.78,3453,78778.73),(45,32),(45)]])