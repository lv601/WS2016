# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:53:24 2016

@author: michael
"""

def generator_func(n):
    i = 1 
    while i < n:
        yield i ** 2 # Creates generator 
        i += 1 
# gen is iterable generator object 
gen = generator_func(10) 
next(gen)
print(next(gen))
next(gen)
print(next(gen))
next(gen)
print(next(gen))