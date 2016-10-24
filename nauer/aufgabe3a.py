#!/usr/bin/env python3

""" Aufgabe 3a
Erstellen Sie ein Zahlenratespiel. Fragen Sie eine Zahl zwischen 1 und 10 vom Benutzer mit der Builtin Funktion input()
ab. Erzeugen Sie eine Zufallszahl mit der Funktion randint() aus dem Modul Random und vergleichen Sie diese mit der
Benutzereingabe. Geben Sie aus, ob der Benutzer die Zahl erraten hat oder ob sie zu hoch oder zu niedrig ist. Beenden
Sie das Spiel, wenn der Benutzer sie erraten hat oder wiederholen Sie die Eingabe bis zu 5 mal.
"""

from random import randint

# Get a random number between 1 and 10
errate = randint(1, 10)
versuche = 5

# Loops through all attempts
for i in range(versuche):
    # Ask for input
    rate = input("Geben Sie eine Zahl zwischen 1 und 10 ein: ")

    # guess right
    if rate == str(errate):
        print("Super! Sie haben die Zahl erraten.")
        break # Leave loop - game finished

    # No attempts left
    if i == versuche - 1:
        print("Sorry, Sie haben verloren. Die Zahl war ",
            errate, "!", sep="")
    # Last attempt
    elif i == versuche - 2:
        print("Sie haben noch 1 Versuch")
    # Next attempt
    else:
        print("Sie haben noch", versuche - i -1, "Versuche")
