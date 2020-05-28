# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:40:49 2017

@author: Arnulfo
"""
from functools import reduce

# Order Number	Book Title and Author	Quantity	Price per Item
orders = [('34587', 'Learning Python', 'Mark Lutz', 4, 40.95),
          ('98762', 'Programming Python', 'Mark Lutz', 5,	56.80),
          ('77226', 'Head First Python', 'Paul Barry', 3,	32.95),
          ('88112', 'Einführung in Python3', 'Bernd Klein', 3, 24.99)]
totals = [(id, quantity*price) for (id, title, author, quantity, price) in orders]
totalsMap = map(lambda total: (total[0], total[1]+10 if total[1] < 100 else total[1]),
        [(id,quantity*price) for (id, title, author, quantity, price) in orders])
for order in totalsMap:
    print(order)

# [ordernumber, (article number, quantity, price per unit),
# ... (article number, quantity, price per unit) ]
# Write a program which returns a list of two tuples with
# (order number, total amount of order).

def total_per_order(detail):
    order_number = detail[0]
    items = detail[1:]
    return (order_number, sum([quantity*price for (id, quantity, price) in items]))

def list_totals(orders):
    return [total_per_order(detail) for detail in orders]

# tutorial solution

orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), 
			              map(lambda x: (x[0],x[2] * x[3]), orders)))

print(invoice_totals)


# The output of the previous program looks like this:
# [('34587', 163.8), ('98762', 284.0), ('77226', 108.85000000000001), ('88112', 84.97)]




orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
	       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
	       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

min_order = 100
invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
invoice_totals = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], invoice_totals))
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), invoice_totals))

print (invoice_totals)
