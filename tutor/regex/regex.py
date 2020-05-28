# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:42:17 2017

@author: Arnulfo
"""

import re
x = re.search("cat","A cat and a rat can't be friends.")
if re.search("cat","A cat and a rat can't be friends."):
    print("Some kind of cat has been found :-)")
else:
    print("No cat has been found :-)")

if re.search("cow","A cat and a rat can't be friends."):
    print("Cats and Rats and a cow.")
else:
    print("No cow around.")


fh = open("simpsons_phone_book.txt")
for line in fh:
    if re.search(r"J.*Neu",line):
        print(line.rstrip())
fh.close()

line = "He is a German called Mayer."
if re.search(r"M[ae][iy]er",line): print("I found one!")

s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."
print(re.search(r"M[ae][iy]er", s1))
print(re.search(r"M[ae][iy]er", s2))
print(re.match(r"M[ae][iy]er", s1))
print(re.match(r"M[ae][iy]er", s2))

print(re.search(r"^M[ae][iy]er", s1))
print(re.search(r"^M[ae][iy]er", s2))

s = s2 + "\n" + s1
print(re.search(r"^M[ae][iy]er", s))
print(re.search(r"^M[ae][iy]er", s, re.MULTILINE))
print(re.search(r"^M[ae][iy]er", s, re.M))
print(re.match(r"^M[ae][iy]er", s, re.M))

print(re.search(r"Python\.$","I like Python."))
print(re.search(r"Python\.$","I like Python and Perl."))
print(re.search(r"Python\.$","I like Python.\nSome prefer Java or Perl."))
print(re.search(r"Python\.$","I like Python.\nSome prefer Java or Perl.", re.M))

mo = re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
print(mo.group())
print(mo.span())
print(mo.start())
print(mo.end())
print(mo.span()[0])
print(mo.span()[1])

fh = open("tags.txt")
for i in fh:
     res = re.search(r"<([a-z]+)>(.*)</\1>",i)
     print(res.group(1) + ": " + res.group(2))
fh.close()

l = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

for i in l:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
    print(res.group(3) + " " + res.group(2) + " " + res.group(1))
    
s = "Sun Oct 14 13:47:03 CEST 2012"
expr = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)\b"
x = re.search(expr,s)
print(x.group('hours'))
print(x.group('minutes'))
print(x.start('minutes'))
print(x.end('minutes'))
print(x.span('seconds'))

t="A fat cat doesn't eat oat but a rat eats bats."
mo = re.findall("[force]at", t)
print(mo)

courses = "Python Training Course for Beginners: 15/Aug/2011 - 19/Aug/2011;Python Training Course Intermediate: 12/Dec/2011 - 16/Dec/2011;Python Text Processing Course:31/Oct/2011 - 4/Nov/2011"
items = re.findall("[^:]*:[^;]*;?", courses)
print(items)
items = re.findall("([^:]*):([^;]*;?)", courses)
print(items)

lines = ["surname: Obama, prename: Barack, profession: president", "surname: Merkel, prename: Angela, profession: chancellor"]
for line in lines:
    re.split(",* *\w*: ", line)[1:]
    