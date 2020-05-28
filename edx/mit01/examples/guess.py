# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:53:09 2017

@author: Arnulfo
"""
challange = "Please think of a number between 0 and 100!"
check = 'Is your secret number '
prompt0 ="Enter 'h' to indicate the guess is too high. "
prompt1 = "Enter 'l' to indicate the guess is too low. "
prompt2 = "Enter 'c' to indicate I guessed correctly."
invalid = "Sorry, I did not understand your input."
done = "Game over. Your secret number was: "
def guess(low,high):
    import numpy
    return numpy.right_shift(low+high, 1)    
print(challange)
low = 0
high = 100
while(low<high):
    media = guess(low,high)
    print(check+str(media)+"?")
    answer = input (prompt0+prompt1+prompt2) 
    if answer == 'c':
        print(done + str(media))
        break
    elif answer == 'l':
        low = media
    elif answer == 'h':
        high = media
    else:
        print(invalid)
    
    