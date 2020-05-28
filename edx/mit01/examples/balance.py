# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 23:18:12 2017

@author: Arnulfo
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

# Test Case 1:
	      balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
                    
          # To make sure you are doing calculation correctly, this is the 
          # remaining balance you should be getting at each month for this example
            Month 1 Remaining balance: 40.99
            Month 2 Remaining balance: 40.01
            Month 3 Remaining balance: 39.05
            Month 4 Remaining balance: 38.11
            Month 5 Remaining balance: 37.2
            Month 6 Remaining balance: 36.3
            Month 7 Remaining balance: 35.43
            Month 8 Remaining balance: 34.58
            Month 9 Remaining balance: 33.75
            Month 10 Remaining balance: 32.94
            Month 11 Remaining balance: 32.15
            Month 12 Remaining balance: 31.38
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def newBalance(balance):
    return balance*(1-monthlyPaymentRate)*(1+annualInterestRate/12)
new = balance
for i in range(12):
    new = newBalance(new)
print('Remaining balance: '+str(round(new,2)))
    