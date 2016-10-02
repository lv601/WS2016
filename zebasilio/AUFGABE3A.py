# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:15:28 2016

@author: jose
"""

from random import randint
errate = randint (1, 10)
versuche = 5
for i in range (versuche):
    rate = input (" Geben Sie eine Zahl zwischen 1 und 10 ein: ")
    if rate == str (errate):
        print("Super!")
        break

    


    
    