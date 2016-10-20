#!/usr/bin/env python3

## Date: 19.10.2016
## Author: Anna Majewski
## Description: Ratespiel umschreiben fuer Konsole

from random import randint
from argparse import ArgumentParser

def guess_game(args):
    """number guess game in range from 'min' to 'max', with 'guesses' guesses"""
    zahl = randint(*args.bereich)
    # Anzahl der Wuerfe

    print("Willkommen beim Ratespiel. Erraten Sie eine Zahl zwischen", args.bereich[0], "und", args.bereich[1], "!")
    for x in range(args.anzahl):
        # Eingabe wird direkt in einer Variable gespeichert.
        eingabe = input("Geben Sie Ihre Zahl ein: ")
        # Die Zahl wird von einem String zu einem Integer umgewandelt.
        eingabe = int(eingabe)
        if eingabe == zahl:
            print ("SUPER! Du hast die Zahl", zahl,"erraten!")
            return
        elif eingabe < zahl:
            print("Zu niedrig. Die Zahl ist groesser!", "Sie haben noch", args.anzahl-1-x, "Versuche!")
        elif eingabe > zahl:
            print("Zu hoch. Die Zahl ist kleiner!", "Sie haben noch", args.anzahl-1-x, "Versuche!")
    else:
            print ("Sie haben leider verloren. Versuchen Sie es noch einmal!")

parser = ArgumentParser() # Konstruktor

parser.add_argument("-b", "--bereich", help="Bereich fuer die Gewinnzahl. [von - bis]", type=int, default=[1,5], nargs=2)
parser.add_argument("-a", "--anzahl", help="Anzahl der Wuerfe.", type=int, default=3)
parser.set_defaults(func=guess_game) #Funktion wird zugewiesen, die als Standard ausgefuehrt wird

args = parser.parse_args()
args.func(args) #Funktion wird mit Argumenten aufgerufen.

