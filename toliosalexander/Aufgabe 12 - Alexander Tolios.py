### Aufgabe 12 - Alexander Tolios - last modified am 29.10.2016
# Aufgabe 5b umgeändert!

from argparse import ArgumentParser
from random import randint

def ratespiel(args):
    print("Ratespiel: Finde die Zahl zwischen", args.range[0], "und", args.range[1], ".")
    cnr = randint(*args.range)
    
    for i in range(args.tryouts):
        enter = input("Bitte Zahl eingeben: ")
        enter = int(enter)
        if enter == cnr:
            print ("Korrekt, die gesuchte Zahl lautet", cnr, "!")
            return
        elif enter < cnr:
            print("Das ist falsch, die gesuchte Zahl ist höher. Noch", args.tryouts-(i+1), "Versuche.")
        elif enter > cnr:
            print("Das ist falsch, die gesuchte Zahl ist niedriger. Noch", args.tryouts-(i+1), "Versuche.")
    else:
            print ("Verloren! Die gesuchte Zahl war:", cnr)

parser = ArgumentParser() # von argparse

# Add new option - ist mit minus
# Add new argument - ist ohne minus
# parser.add_argument("input", help="Input file")
# parser.add_argument("-o", "--output", dest="out", default="-", help="Output file") # default="-" ist ein pseudo-Eleement, führt zu einem stdout auf die Konsole, nicht in ein file
parser.add_argument("-r", "--range", help="Range of the correct number", type=int, default=[0,9], nargs=2)
parser.add_argument("-t", "--tryouts", help="Number of tryouts", type=int, default=3)
parser.set_defaults(func=ratespiel) # Default-Funktion

# Read in command line arguments
args = parser.parse_args()
args.func(args) # Std-Funktion mit Argumenten args

