# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:16:38 2017

@author: Arnulfo
"""

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv',index_col=0)

# Print out cars
print(cars)

# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]] )

# Print out observation for Japan
print(cars.loc[['JAP']])

# Print out observations for Australia and Egypt
print(cars.loc[["AUS","EG"]])

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])