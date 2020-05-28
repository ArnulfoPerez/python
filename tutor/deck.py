# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:12:41 2017

@author: Arnulfo
"""

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