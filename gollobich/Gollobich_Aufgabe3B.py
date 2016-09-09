# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:41:43 2016

@author: Martin Gollobich"""

string = input("Geben sie einen String ein")

ws = 3

string=str(string)

for i in range(0, len(string) - ws + 1):
    print(" " * i, string[i:i + ws], sep=str(i)+")")

