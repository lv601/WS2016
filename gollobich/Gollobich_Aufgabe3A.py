# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:09:12 2016

@author: Martin Gollobich
"""

from random import randint
z=randint(1,10)
print(z)

versuche=5

for i in range (versuche):
    x=input("Geben sie eine Zahl von 1 bis 10 ein")
    x=int(x)
    if i == versuche-2:
        print("Nur noch ein Versuch")
    if x==z:
        print("Richtige Zahl")
        break
    elif x<z:
        print("Die eingegebene Zahl war kleiner")
        
    elif x>z:
        print("Die eingegebene Zahl war größer")
        
  
    if i == versuche-1:
        print("Sie haben verloren")


