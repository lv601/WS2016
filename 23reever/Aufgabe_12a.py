#!/usr/bin/python3.5
# Aufgabe 12, Grundlage: Aufgabe 5b
# Funktionsparameter = randit, wiederholungen als Kommandozeilenparameter

from argparse import ArgumentParser
import argparse

from random import randint

def ratespiel(args):
    zufallszahl = randint(1, args.limit)
    #wiederholungen = 5
    #user = input("Rate eine Zahl zwischen 1 und 10: ")

    for i in range(args.repeat):

# Nach Zahl fragen - Input von User
        user = int(input("Rate eine Zahl zwischen 1 und {}: ".format(args.limit))) #sonst wird input als str gelesen und Reihenfolge wäre 1, 10, 2, 3... 9

# 1. Fall: Antwort von user ist richtig
        if  user == zufallszahl:
            print("Gratuliere! Die Zahl ist richtig.")
            # schleife wird beendet
            break

# 2a Fall: Zahl war zu hoch:
        if user > zufallszahl:
            print("Die Zahl ist zu hoch. Du hast noch", args.repeat - i -1, "Vesuche.")

# 2b Fall: Zahl war zu niedrig:
        if user < zufallszahl:
            print("Die Zahl ist zu niedrig. Du hast noch", args.repeat - i -1, "Vesuche.")

# 3. Fall Zahl wird nicht erraten
        if i == args.repeat - 1:
            print("Du hast leider verloren. Die gesuchte Zahl ist: ", zufallszahl, "!")
            break

parser = argparse.ArgumentParser(prog='SPIEL')
parser.add_argument("-r", "--repeat", help="Anzahl der Wiederholungen", type=int, default=5)
parser.add_argument("-l", "--limit", help="Höchste mögliche Zahl", type=int, default=10)
#args = parser.parse_args()
#print(args.repeat)

# TIPP: man kann mit set_defaults eine Startfunktion definieren, die man einfach aufgerufen kann. Das ist besonders
# nützlich, wenn man mit Subparsern arbeitet. Jedem Subparser wird eine Startfunktion zugewiesen und automatisch mit
# args.func(args) gestartet
parser.set_defaults(func=ratespiel)
args = parser.parse_args()
args.func(args)

#ratespiel(args.limit, args.repeat)