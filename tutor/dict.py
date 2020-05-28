# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 22:26:54 2017

@author: Arnulfo
"""

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
country_specialities_zip = zip(dishes,countries)
print(list(country_specialities_zip))
country_specialities_list = list(country_specialities_zip)
country_specialities_dict = dict(country_specialities_list)
print(country_specialities_dict)

country_specialities_dict = dict(zip(dishes,countries))
print(country_specialities_dict)

adjectives = {"cheap","expensive","inexpensive","economical"}
