# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 23:53:31 2017

@author: Arnulfo
"""

cities = ["Paris", "Berlin", "Hamburg", "Frankfurt", "London", "Vienna", "Amsterdam", "Den Haag"]
for location in cities:
    print("location: " + location)
expertises = ["Novice", "Beginner", "Intermediate", "Proficient", "Experienced", "Advanced"]
expertises_iterator = iter(expertises)
assert next(expertises_iterator) == 'Novice'
assert next(expertises_iterator) == 'Beginner'
assert next(expertises_iterator) == 'Intermediate'
assert next(expertises_iterator) == 'Proficient'
assert next(expertises_iterator) == 'Experienced'
assert next(expertises_iterator) == 'Advanced'
other_cities = ["Strasbourg", "Freiburg", "Stuttgart", 
                "Vienna / Wien", "Hannover", "Berlin", 
                "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break
    
def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
city = city_generator()
assert next(city) == "London"
assert next(city) == "Hamburg"
assert next(city) == "Konstanz"
assert next(city) == "Amsterdam"
assert next(city) == "Berlin"
assert next(city) == "Zurich"
assert next(city) == "Schaffhausen"
assert next(city) == "Stuttgart"

def fibonacci():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

counter = 0
for x in f:
    print(x, " ", end="")
    counter += 1
    if (counter > 10): 
        break 
print()

