# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:10:40 2017

@author: Arnulfo
"""

q = 459
p = 0.098
print(q, p, p * q)
print(q, p, p * q, sep=",")
print(q, p, p * q, sep=" :-) ")
 
# Alternatively, we can construe out of the values a new string 
# by using the string concatenation operator:
print(str(q) + " " + str(p) + " " + str(p * q))
print("%10.3e"% (356.08977))
print("%10.3E"% (356.08977))
print("%10o"% (25))
print("%10.3o"% (25))
print("%10.5o"% (25))
print("%10x"% (47))
print("%10.4x"% (47))
print("%10.4X"% (47))
print("Only one percentage sign: %% " % ())

print("%#5X"% (47))
print("%5X"% (47))
print("%#5.4X"% (47))
print("%#5o"% (25))
print("%+d"% (42))
print("% d"% (42))
print("%+2d"% (42))
print("% 2d"% (42))
print("%2d"% (42))

print("First argument: {0}, second one: {1}".format(47,11))
print("Second argument: {1}, first one: {0}".format(47,11))
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11))
print("First argument: {}, second one: {}".format(47,11))
print('First argument: 47, second one: 11')
# arguments can be used more than once:
print("various precisions: {0:6.2f} or {0:6.3f}".format(1.4148))

print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058))

print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))

print("The capital of {0:s} is {1:s}".format("Ontario","Toronto"))
print("The capital of {province} is {capital}".format(province="Ontario",capital="Toronto"))

data = dict(province="Ontario",capital="Toronto")
print("The capital of {province} is {capital}".format(**data))
# The double "*" in front of data turns data automatically
# into the form 'province="Ontario",capital="Toronto"'. 
# Let's look at the following Python program:
capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    print("{country}: {capital}".format(country=c, capital=capital_country[c]))
    
print("Countries and their capitals:")
for c in capital_country:
    format_string = c + ": {" + c + "}" 
    print(format_string.format(**capital_country))
    
a = 42
b = 47
def f(): return 42
locals()
# The dictionary returned by locals() can be used as a parameter of the string format method. This way we can use all the local variable names inside of a format string. 

# Continuing with the previous example, we can 
# create the following output, in which we use the local variables a, b and f:
print("a={a}, b={b} and f={f}".format(**locals()))

s = "Python"
print(s.center(10))
print(s.center(10,"*"))

s = "Programming"
print(s.rjust(15))
print(s.rjust(15, "~"))
account_number = "43447879"
print(account_number.zfill(12))
print(account_number.rjust(12,"0"))


