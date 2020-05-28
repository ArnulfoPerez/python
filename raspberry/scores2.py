# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:43:31 2019

@author: arnulfo
"""

list_of_names = '54 - Alice,35 - Bob,27 - Carol,27 - Chuck,05 - Craig,30 - Dan,27 - Erin,77 - Eve,14 - Fay,20 - Frank,48 - Grace,61 - Heidi,03 - Judy,28 - Mallory,05 - Olivia,44 - Oscar,34 - Peggy,30 - Sybil,82 - Trent,75 - Trudy,92 - Victor,37 - Walter'

scores = [[int(x[0]),x[1]]for x in [item.split('-') for item in list_of_names.split(',')]]


# sort list with key
scores.sort(key=lambda x: x[0],reverse=True)

# print list
print('Sorted list:', scores)