# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:15:37 2017

@author: Arnulfo
"""

from random import randint

def grange(ini,end,inc=1,lst = lambda x,y: x < y,add = lambda x,y: x + y):
    value = ini
    while lst(value,end):
        yield value
        value = add(value,inc)
        
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

f = open('times_and_temperatures.txt', 'w')
f.write('Time and temperature\n')

for x in trange((6,0,0),(6,10,0),(0,0,90)):
    h,m,s = x
    f.write('{0:2d}:{1:0>2}:{2:0>2}  {3:2.1f}\n'.format(h,m,s,randint(100,250)/10))
f.close()