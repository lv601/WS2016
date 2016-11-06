# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:01:28 2016

@author: jose
"""

from random import randint



def game(val1, val2, attempts):
    number = randint (val1, val2)
    guess = attempts
    print("Welcome to the Game. Geben Sie eine Zahl zwischen", val1, "und", val2, "ein")
    for i in range(guess):
        rate = input("Geben Sie eine Zahl ein:")
        rate = int(rate)        
        if rate == number:
            print("Super!")
            return number
            break
        elif rate < number:
            print("you are to low. the number is higher", "you have still", guess-1-i, "attempts")
        elif rate > number: 
            print("you are to high. the number is lower", "you have still", guess-1-i, "attempts")
game(1, 10, 5)
            
        