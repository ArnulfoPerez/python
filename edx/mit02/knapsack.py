# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:36:05 2017

@author: arnulfo
"""
class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        self.density = value/weight
    def __str__(self):
        return self.name + ": <" +\
                str(self.value) + ", " + str(self.weight) + ">"

def greedy(candidates, capacity, key_function):
    def helper(selected, candidates, weight):
        if candidates:
            test_value = weight + candidates[0].weight
            if test_value > capacity:
                return (selected, weight)
            elif  test_value == capacity:
                return (selected.append(candidates[0]), test_value)
            else:
                selected += [candidates[0]]
                return helper(selected, candidates[1:], test_value)
        else:
            return (selected, weight)
    sorted_items = sorted(candidates, key=key_function, reverse=True)
    if sorted_items[0].weight < capacity:
        return helper([sorted_items[0]], sorted_items[1:], sorted_items[0].weight)
    elif sorted_items[0].weight == capacity:
        return ([sorted_items[0]], [sorted_items[0].weight])
    else:
        return ([], 0)
    
def maxVal(candidates, capacity):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if candidates == [] or capacity == 0:
        return (0, ())
    elif candidates[0].weight > capacity:
        #Explore right branch only
        return maxVal(candidates[1:], capacity)
    else:
        nextItem = candidates[0]
        #Explore left branch
        withVal, withToTake = maxVal(candidates[1:],
                                     capacity - nextItem.weight)
        withVal += nextItem.value
        #Explore right branch
        withoutVal, withoutToTake = maxVal(candidates[1:], capacity)
        #Choose better branch
        if withVal > withoutVal:
            return (withVal, withToTake + (nextItem,))
        else:
            return (withoutVal, withoutToTake)
        
def memoized_max(candidates,capacity):
    cache = {}
    def helper(candidates,capacity):
        length = len(candidates)
        args = (length,capacity)
        if args not in cache:
            cache[args] = maxVal(candidates, capacity)
        return cache[args]
    return helper

items = []
items.append(Item('one', 99, 70))
items.append(Item('two', 94, 7))
items.append(Item('three', 79, 6))
items.append(Item('four', 64, 3))
items.append(Item('five', 50, 60))
items.append(Item('six', 94, 7))
items.append(Item('seven', 46, 6))
items.append(Item('eight', 64, 50))
items.append(Item('nine', 43, 33))
items.append(Item('ten', 37, 33))
items.append(Item('eleven', 32, 33))
items.append(Item('twelve', 19, 11))
items.append(Item('thirteen', 18, 7))
items.append(Item('fourteen', 94, 3))
items.append(Item('fifteen', 46, 16))
items.append(Item('sixteen', 6, 50))

(l, w) = greedy(items, 100, lambda x: -x.weight)
print(sum([s.value for s in l]))
print(w)

(l, w) = greedy(items, 100, lambda x: x.value)
print(sum([s.value for s in l]))
print(w)

(l, w) = greedy(items, 100, lambda x: x.density)
print(sum([s.value for s in l]))
print(w)

value, selected = maxVal(items,100)
print(value)
[print(s) for s in l]

maxValue = memoized_max(items,100)
value, selected = maxVal(items,100)
print(value)
[print(s) for s in l]
