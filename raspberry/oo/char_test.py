# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:09:02 2019

@author: arnulfo
"""

from character import Enemy
dave = Enemy("Dave", "A smelly zombie")

dave.describe()


# Add some conversation for Dave when he is talked to
dave.set_conversation("What's up, dude!")

# Trigger a conversation with Dave
dave.talk()

dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)



