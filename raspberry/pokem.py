# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:32:34 2019

@author: arnulfo
"""

from pokebase import pokemon
from requests import get
from PIL import Image
from io import BytesIO

def fetch_pokemon():
    name = input('Which Pokemon do you want to fetch? ')
    poke = pokemon(name)
    pic = get(poke.sprites.front_default).content
    image = Image.open(BytesIO(pic))
    image.save('poke.gif')
    print(name + ' weighs ' + str(poke.weight))
    print(poke.sprites)

fetch_pokemon()