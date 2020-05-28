# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:32:34 2019

@author: arnulfo
"""
from guizero import App, TextBox, PushButton, Picture


from pokebase import pokemon
from requests import get
from PIL import Image
from io import BytesIO

def fetch_pokemon():
    name = input_box.value
    try:
      poke = pokemon(name)
    except ValueError:
        print("Variable x is not defined")
        return
    except:
        print("Something else went wrong") 
        return
    pic = get(poke.sprites.front_default).content
    image = Image.open(BytesIO(pic))
    image.save('poke.gif')
    icon.value = 'poke.gif'    

app = App(title='Pokemon Fetcher', width=300, height=200)
input_box = TextBox(app, text='Name')
icon = Picture(app, image="poke.gif")
submit = PushButton(app, command=fetch_pokemon, text='Submit')

app.display()