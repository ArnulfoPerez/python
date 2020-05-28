# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:02:02 2017

@author: Arnulfo
"""
import pickle

file_handle = open("cities_and_times.txt", "r")
lines = file_handle.readlines()
file_handle.close()
lines.sort()
cities = []
for line in lines:
    city = line.split()
    (hour,minutes)= city[-1].split(':')
    day = city[-2]
    name =  " ".join(x for x in city[:-2])
    t =(int(hour),int(minutes))
    c=(name,day,t)
    cities.append(c)
fh = open("cities_and_time.pkl", "bw")
pickle.dump(cities, fh)
fh.close()

f = open("cities_and_time.pkl", "rb")
villes = pickle.load(f)
f.close()
print(villes)
