# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:01:28 2016

@author: jose
"""

from random import randint
def game(val1, val2, attempts):
    number = randint (val1, val2)
    guess = attempts
    print ("Welcome to the Game. Geben Sie eine Zahl zwischen", val1, "und", val2, "ein")
    # ACHTUNG: You don't need enumerate() and index here.
    # i is already the index
    # TIPP: You can use the 'else' way from the for loop
    # to add a game over message when all guesses run out
    for index, i in enumerate(range(guess)):
        # TIPP: Do not seperate function name and
        # function parameter brackets with spaces
        # This is very uncommon and looks really ugly
        rate = input ("Geben Sie eine Zahl ein:")
        rate = int (rate)        
        if rate == number:
            print ("Super!")
            # TIPP: You can also use return here to leave the
            # function and add a return value. So other functions
            # can work with that.
            break
        elif rate < number:
            print ("you are to low. the number is higher", "you have still", guess-1-index, "attempts")
        elif rate > number: 
            print ("you are to high. the number is lower", "you have still", guess-1-index, "attempts")
game(1, 10, 5)
            
        