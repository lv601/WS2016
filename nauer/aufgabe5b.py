#!/usr/bin/env python3

""" Aufgabe 5b
Schreiben Sie das Ratespiel von Aufgabe 3a so um damit sie eine Funktion verwenden
"""
from random import randint

def run_game(bereich, versuche):
    errate = randint(*bereich) # unpack tuple

    # Loops through all attempts
    for i in range(versuche):
        # Ask for input
        rate = int(input("Geben Sie eine Zahl zwischen {0} un {1} ein: ".format(*bereich)))

        # guess right
        if rate == errate:
            print("Super! Sie haben die Zahl erraten.")
            return errate
        elif rate < errate:
            print("Zu niedrig!")
        else:
            print("Zu hoch!")

        # Last attempt
        if versuche - 1 > i >= 0:
            if i == versuche - 2:
                print("Sie haben noch 1 Versuch")
            # Next attempt
            else:
                print("Sie haben noch {} Versuche".format(versuche - i - 1))
    else:
        # No attempts left
        print("Sorry, Sie haben verloren. Die Zahl war {}!".format(errate))
        return None

while run_game((3, 7), 4):
    print("\nSehr gut! Gleich das nächste Spiel\n")
else:
    print("\nGame Over\n")
