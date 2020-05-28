# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 23:45:15 2017

@author: Arnulfo
"""

balance = 3329
annualInterestRate = 0.2
monthlyPayment = max(10,balance//12)
monthlyPayment = (monthlyPayment//10)*10

def newBalance(balance):
    return (balance-monthlyPayment)*(1+annualInterestRate/12)
def annualBalance():   
    new = balance
    for i in range(12):
        new = newBalance(new)
    return new
while annualBalance() > 0:
    monthlyPayment += 10
print('Lowest Payment: '+str(monthlyPayment))