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
        # TIPP: Hier können Sie nun den übersichtlicheren format String verwenden
        # "Geben sie eine Zahl von {0} bis {2} ein".format(*bereich)
        x=input("Geben sie eine Zahl von "+str(bereich[0])+" bis "+str(bereich[-1])+" ein")
        x=int(x)
        if i == versuche-2:
            print("Nur noch ein Versuch")
        if x==z:
            print("Richtige Zahl")
            # TIPP: Anstatt nur die Schleife zu verlassen, können Sie mit return
            # auch gleich die Funktion verlassen und auch gleich einen Rückgabewert
            # mitgeben. Z.B. bei Erfolg die erratete Zahl und bei nicht Erfolg None
            # zurückgeben. Somit können Sie den Rückgabewert der Funktion in andern
            # Funktionen mitverabrbeiten, wenn gewünscht.
            #    return x
            #    return None # in Zeile 45
            break
        elif x<z:
            print("Die eingegebene Zahl war kleiner")
            
        elif x>z:
            print("Die eingegebene Zahl war größer")
            
      
        if i == versuche-1:
            print("Sie haben verloren")
    
    
ratespiel((int(input("geben sie den Anfang des Bereiches ein")),int(input("Ende"))),int(input("Anzahl der Versuche")))
