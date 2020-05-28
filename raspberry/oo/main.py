# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:10:54 2019

@author: arnulfo
"""

from room import Room
from character import Enemy

dave = Enemy("Dave", "A smelly zombie")

# Add some conversation for Dave when he is talked to
dave.set_conversation("What's up, dude!")

dave.set_weakness("cheese")

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dining_hall.set_character(dave)



current_room = dining_hall

while True:		
    print("\n")         
    current_room.get_details()   
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()      
    command = input("> ")    
    current_room = current_room.move(command)  