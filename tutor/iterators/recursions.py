# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:49:13 2017

@author: Arnulfo
"""

def times_three(dummy):
    ''' Multiplies by 3 using recursion'''
    return 3 if dummy == 1 else times_three(dummy-1) + 3

def pascal_triangle(level):
    '''Generates a Pascal triangle of level + 1 rows'''
    if level == 0:
        return [[1]]
    else:
        triangle = pascal_triangle(level-1)
        top = triangle[-1]
        last = [1]
        for i in range(1, level):
            last.append(top[i-1] + top[i])
        last.append(1)
        triangle.append(last)
        return triangle
def fibp(num):
    '''Generates Fibonnaci numbers using recursion and Pascal triangle'''
    def acc(row, column):
        '''Inner helper function'''
        if row == column or row == (column + 1):
            return triangle[row][column]
        else:
            return triangle[row][column] + acc(row - 1, column + 1)
    if num == 0:
        return 0
    else:
        triangle = pascal_triangle(num)
        return acc(num - 1, 0)
def find_index(fibonnaci):
    '''Finds index of number n in a Fibonnaci sequence'''
    def inner(old, new, i):
        '''Recursive helper function'''
        if new == fibonnaci:
            return i
        if new > fibonnaci:
            return -1
        return inner(new, old + new, i + 1)
    if fibonnaci == 0:
        return 0
    if fibonnaci == 1:
        return 1
    return inner(1, 1, 2)
def primes_gen():
    '''Prime number generator'''
    sieve = []
    i = 2
    def is_non_prime(i):
        '''Returns True if the argument is not prime'''
        for prime in sieve:
            if i % prime == 0:
                return True
        return False
    while True:
        yield i
        sieve.append(i)
        i += 1
        while is_non_prime(i):
            i += 1
def primes(limit):
    '''Finds all primes less or equal to n'''
    def inner(prime_list, sieve):
        '''Recursive helper function'''
        def is_prime(num):
            '''Returns True if num is prime'''
            for prime in prime_list:
                if num % prime == 0:
                    return False
            return True
        if sieve == []:
            return prime_list
        else:
            if is_prime(sieve[0]):
                prime_list.append(sieve[0])
            return inner(prime_list, sieve[1:limit])
    if limit == 2:
        return [2]
    return inner([2], [x for x in range(3, limit + 1)])

assert primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
assert times_three(7) == 21
assert pascal_triangle(0) == [[1]]
assert pascal_triangle(1) == [[1], [1, 1]]
assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
assert pascal_triangle(4) == \
                      [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal_triangle(5) == \
 [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
assert fibp(0) == 0
assert fibp(1) == 1
assert fibp(2) == 1
assert fibp(3) == 2
assert fibp(4) == 3
assert fibp(5) == 5
assert fibp(6) == 8
assert fibp(7) == 13
assert find_index(2) == 3
assert find_index(3) == 4
assert find_index(4) == -1
assert find_index(5) == 5
assert find_index(6) == -1
assert find_index(7) == -1
assert find_index(8) == 6
assert find_index(9) == -1
assert find_index(10) == -1
assert find_index(11) == -1
assert find_index(12) == -1
assert find_index(13) == 7
                 