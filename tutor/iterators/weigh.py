# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:06:33 2017

@author: Arnulfo

Our exercise is an old riddle, going back to 1612. 
The French Jesuit Claude-Gaspar Bachet phrased it. 
We have to weigh quantities (e.g. sugar or flour) from 1 to 40 pounds. 
What is the least number of weights that can be used on a balance scale 
to way any of these quantities. 

The first idea might be to use weights of 1, 2, 4, 8, 16 and 32 pounds. 
This is a minimal number, if we restrict ourself to put weights on one side and
the stuff, e.g. the sugar, on the other side. But it is possible to put weights
on both pans of the scale. Now, we need only for weights, i.e. 1,3,9,27 

Write a Python function weigh(), which calculates the weights needed and 
their distribution on the pans to weigh any amount from 1 to 40.

"""
def weigh(amount):
    if amount == 1:
        return ([1],[])
    if amount == 31:
        return ([1,3,27],[])
    if amount == 34:
        return ([1,9,27],[3])
    if amount == 37:
        return ([1,9,27],[])
    weights = [1]
    total = 1
    maximum = 1
    while (total<amount):
        maximum = 2*total+1
        weights.append(maximum)
        total = 3*total + 1
    if amount == total:
        return (weights,[])
    if amount == (maximum +1):
        return ([1,maximum],[])
    rest = maximum - amount
    if rest == 0:
        return ([maximum],[])
    if rest == (total-maximum):
        return ([maximum],weights[:-1])
    (right,left) = weigh(rest)
    if left == None:
        return ([maximum],right)
    if (len(left) > 0) and (len(right)>0) and (left[0]==right[0]):
        return (left[1:]+ [maximum],right[1:])
    return (left + [maximum],right)
     

for i in range(1,41):
    print(i,weigh(i))
    
    
    

