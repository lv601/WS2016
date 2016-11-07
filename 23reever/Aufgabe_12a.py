#!/usr/bin/python3.5
# Aufgabe 12, Grundlage: Aufgabe 5b
# Funktionsparameter = randit, wiederholungen als Kommandozeilenparameter

from argparse import ArgumentParser
import argparse

from random import randint

def ratespiel(max, wiederholungen):
    zufallszahl = randint(1, max)
    #wiederholungen = 5
    #user = input("Rate eine Zahl zwischen 1 und 10: ")

    for i in range(wiederholungen):

# Nach Zahl fragen - Input von User
        user = int(input("Rate eine Zahl zwischen 1 und " + str(max) + ": ")) #sonst wird input als str gelesen und Reihenfolge wäre 1, 10, 2, 3... 9

# 1. Fall: Antwort von user ist richtig
        if  user == zufallszahl:
            print("Gratuliere! Die Zahl ist richtig.")
            # schleife wird beendet
            break

# 2a Fall: Zahl war zu hoch:
        if user > zufallszahl:
            print("Die Zahl ist zu hoch. Du hast noch", wiederholungen - i -1, "Vesuche.")

# 2b Fall: Zahl war zu niedrig:
        if user < zufallszahl:
            print("Die Zahl ist zu niedrig. Du hast noch", wiederholungen - i -1, "Vesuche.")

# 3. Fall Zahl wird nicht erraten
        if i == wiederholungen - 1:
            print("Du hast leider verloren. Die gesuchte Zahl ist: ", zufallszahl, "!")
            break

parser = argparse.ArgumentParser(prog='SPIEL')
parser.add_argument("-r", "--repeat", help="Anzahl der Wiederholungen", type=int, default=5)
parser.add_argument("-l", "--limit", help="Höchste mögliche Zahl", type=int, default=10)
args = parser.parse_args()
#print(args.repeat)

ratespiel(args.limit, args.repeat)