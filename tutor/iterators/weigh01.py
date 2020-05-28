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

class Weights:
    '''
    Memoization decorator class
    '''
    def __init__(self):
        self.weights = {1:[1]}
        self.total = 1
    def get_total(self, amount):
        '''
        As we are using a dictionary, we can't use mutable arguments,
        i.e. the arguments have to be immutable.
        '''
        while self.total < amount:
            weights = self.weights[self.total] + [2 * self.total + 1]
            self.total = 3 * self.total + 1
            self.weights[self.total] = weights
        dummy = 1
        while dummy < amount:
            dummy = 3 * dummy + 1
        return dummy
def weigh(amount):
    '''
    Calculates the weights needed and their distribution
    on the pans to weigh any amount
    '''
    def get_weights(amount):
        '''
        helper function
        '''
        if amount == 1:
            return ([1], [])
        total = weight_set.get_total(amount)
        weights = weight_set.weights[total]
        if amount == total:
            return (weights, [])
        maximum = weights[-1]
        if amount == maximum:
            return ([maximum], [])
        elif amount < maximum:
            (_right, _left) = get_weights(maximum-amount)
        else:
            (_left, _right) = get_weights(amount-maximum)
        _left += [maximum]
        return (_left, _right)
    if amount < 1:
        return ([], [])
    weight_set = Weights()
    return get_weights(amount)
# test
for i in range(0, 41):
    (left, right) = weigh(i)
    assert sum(left) == (sum(right) + i )
        