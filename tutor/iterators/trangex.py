# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:47:09 2017

@author: Arnulfo
"""

def grange(ini,end,inc=1,lst = lambda x,y: x < y,add = lambda x,y: x + y):
    value = ini
    while lst(value,end):
        message = yield value
        if message == None:
            value = add(value,inc)
        else:
            value = ini
        
def time_lst(a,b):
    h1,m1,s1 = a
    h2,m2,s2 = b
    if h1 < h2:
        return True
    if m1 < m2:
        return True
    if s1 < s2:
        return True
    return False

def time_add(a,b):
    hour1,min1,sec1=a
    hour2,min2,sec2=b
    secs = sec1 + sec2
    mins = min1 + min2 + (secs//60)
    return (hour1 + hour2 + (mins//60),mins % 60,secs % 60)

def trange(ini,end,inc=(0,0,1)):
    return grange(ini,end,inc,lst=time_lst,add=time_add)

a = (20,22,50)
b = (20, 45, 50)
assert time_lst(a,b) == True 
assert time_lst(b,a) == False
assert time_lst(b,b) == False             
assert time_add(a,b) == (41,8,40)

for i in grange(a,b,(0,0,1),lst=time_lst,add=time_add):
    print(i)
print()    
for i in trange(a,b,(0,10,1)):
    print(i)

ini = 0
end = 5
inc = 3
test = ini
for i in grange(ini,end):
    assert i == test
    test += 1
test = ini  
for i in grange(ini,end,inc):
    assert i == test
    test += inc