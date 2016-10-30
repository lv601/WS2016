# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 09:45:26 2016

@author: jose
"""
#!/usr/bin/env python3


from random import randint
import argparse

def game(val1, val2, attempts):
    number = randint (val1, val2)
    guess = attempts
    print("Welcome to the Game. Type in a number between", val1, "and", val2)
    for i in range(guess):
        rate = input("Type in a number:")
        rate = int(rate)        
        if rate == number:
            print("Super!")
            return number
            break
        elif rate < number:
            print("you are to low. the number is higher", "you have still", guess-1-i, "attempts")
        elif rate > number: 
            print("you are to high. the number is lower", "you have still", guess-1-i, "attempts")


parser = argparse.ArgumentParser(description='game')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='A number between 1 and 10')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


game(1, 10, 5)

#file name:Aufgabe12.py
#in the command line: chmod +x Aufgabe12.py
#python Aufgabe12.py 1 10 5

