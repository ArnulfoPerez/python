# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 00:12:21 2017

@author: Arnulfo
"""

balance = 320000
annualInterestRate = 0.2
low = max(balance/12,0.01)
high = low*(1+annualInterestRate)*2

def newBalance(balance,monthlyPayment):
    return (balance-monthlyPayment)*(1+annualInterestRate/12)
def annualBalance(monthlyPayment):   
    new = balance
    for i in range(12):
        new = newBalance(new,monthlyPayment)
    return new
def searchLow(low,high):
    monthlyPayment = (low+high)/2
    test = annualBalance(monthlyPayment)
    if abs(test) < .01:
        return monthlyPayment
    elif test > 0:
        return searchLow(monthlyPayment,high)
    else:
        return searchLow(low,monthlyPayment)
print('Lowest Payment: '+str(round(searchLow(low,high),2)))
