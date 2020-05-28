# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:17:34 2017

@author: Arnulfo
"""

def fibogen():
    fib_1 = 1
    fib_2 = 0
    while True:
        next = fib_1 + fib_2
        yield next
        fib_2 = fib_1
        fib_1 = next
        
def genPrimes():
    primes = [2]
    yield 2
    candidate = 2
    while True:
        flag = True
        candidate += 1
        for factor in primes:
            if (candidate % factor == 0):
                flag = False
                break
        if flag:
            primes.append(candidate)
            yield candidate
        

for n in genPrimes():
    if n > 1000:
        break
    print(n)