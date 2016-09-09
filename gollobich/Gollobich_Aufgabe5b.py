# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:48:58 2016

@author: Gollobich
"""

from random import randint

def ratespiel(bereich,versuche):

    z=randint(*bereich)
    print(z,"ist die richtige Zahl")
    print("Bereich = "+str(bereich))
    print("Versuche = "+str(versuche))
    
    
    
    for i in range (versuche):
        x=input("Geben sie eine Zahl von "+str(bereich[0])+" bis "+str(bereich[-1])+" ein")
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
    
    
ratespiel((int(input("geben sie den Anfang des Bereiches ein")),int(input("Ende"))),int(input("Anzahl der Versuche")))
