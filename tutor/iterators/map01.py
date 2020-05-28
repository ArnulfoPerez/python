# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:56:51 2017

@author: arnulfo
"""

orders =[
        ['34587', 'Learning Python', 'Mark Lutz', 4, 40.95],
        ['98762', 'Programming Python', 'Mark Lutz', 5, 56.80],
        ['77226', 'Head First Python', 'Paul Barry', 3, 32.95],
        ['88112', 'Einführung in Python3', 'Bernd Klein',	3, 24.99]]
min_order = 100

print([(id,quantity*price if quantity*price > min_order else quantity*price + 10 ) 
    for [id,title,author,quantity,price] in orders])

temp = [(id,round(quantity*price,2) ) for id,title,author,quantity,price in orders] 

print([(id,total if total > min_order else total + 10 ) for id,total in temp])

invoices = map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),
    map(lambda x: (x[0],round(x[3] * x[4],2)), orders))
print(list(invoices))
