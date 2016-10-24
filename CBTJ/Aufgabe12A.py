#!/usr/bin/env python3

from argparse import ArgumentParser
from random import randint


def gluecksrad(versuche):
    zufallszahl = randint(1, 10)
    for i in range(versuche):
        eingabe = input("Geben Sie eine Zahl zwischen 1 und 10 ein: ")
        glueckszahl = eingabe
        if zufallszahl == int(glueckszahl):
            print ("Sie haben gewonnen!")

            return zufallszahl


        else:
            if i < (versuche-1):
                print ("Versuchen Sie es noch einmal!")

    else:
        print ("Leider nein")
        print("Die richtige Zahl lautet: {}".format(zufallszahl))

        return None


parser = ArgumentParser()
parser.add_argument('versuche', type=int, help='Anzahl der Versuche')
args = parser.parse_args()
ergebnis=gluecksrad(args.versuche)
