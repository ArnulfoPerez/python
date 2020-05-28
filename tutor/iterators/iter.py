# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:53:37 2017

@author: Arnulfo
"""

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

sum(values)

assert set(keys) == set(['eggs', 'bacon', 'sausage', 'spam'])
assert set(values) == set([2, 1, 1, 500])

# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
assert set(keys) == set(['spam', 'bacon'])

# set operations
assert (keys & {'eggs', 'bacon', 'salad'}) == {'bacon'}

r = range(3) 
assert hasattr(r, '__next__') == False

it = iter(r)
assert next(it) == 0

d = {'a': 0, 'b': 1, 'c': 2}
items = d.items()
assert hasattr(items, '__next__') == False
it = iter(items)
print(next(it))
# ('b', 1)
print(next(it))
# ('c', 2)
print(next(it))
# ('a', 0)

class mylist(list):
    def __iter__(self, *a, **kw):
        print('id of iterable is still:', id(self))
        rv = super().__iter__(*a, **kw)
        print('id of iterator is now:', id(rv))
        return rv 

l = mylist('abc')
# A for loop can use the iterable object and will implicitly get an iterator

for c in l:
    print(c)
# A subsequent for loop can use the same iterable object, but will get another iterator

for c in l:
    print(c)
# id of iterable is still: 139696242511768
# id of iterator is now: 139696242445616
# a
# b
# c
# We can also obtain an iterator explicitly

it = iter(l)
# id of iterable is still: 139696242511768
# id of iterator is now: 139696242463688
# but it can then only be used once
    
class Card(object):
    def __init__(self, rank, suit):
        FACE_CARD = {11: 'J', 12: 'Q', 13: 'K'}
        self.suit = suit
        self.rank = rank if rank <=10 else FACE_CARD[rank]
    def __str__(self):
        return "%s%s" % (self.rank, self.suit)
    
class Deck(object):
    def __init__(self):
        self.cards = []
        for s in ['S', 'D', 'C', 'H']:
            for r in range(1, 14):
                self.cards.append(Card(r, s))
    def __iter__(self):
        return iter(self.cards)
                
for c in Deck().cards: print(c)
for c in Deck(): print(c)
             
             