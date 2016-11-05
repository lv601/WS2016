from random import randint
from argparse import ArgumentParser

def zufallszahlen(args):
    rando = randint(*args.bereich)

    for i in range(args.versuche):
        eingabe = int(input("Ratespiel - geben Sie eine Zahl zwischen " + str(args.bereich[0]) + " und " + str(args.bereich[1]) + " ein:"))

        if rando == eingabe:
            print("richtig Zahl erraten!")
            print("Die Zahl war: ", rando)
            break

        elif rando < eingabe:
            print("Die Zahl ist zu hoch!")

        else:
            print("Die Zahl ist zu niedrig!")

        if i == args.versuche-1:
            print("Sie haben keine Versuche mehr!")
            print("Die erzeugte Zufallszahl war: ", rando)
            break

        print("Sie haben noch ", args.versuche-i-1, " Versuche!")

parser = ArgumentParser()

parser.add_argument("-b", "--bereich", help="Bereich fuer die Gewinnzahl. [von - bis]", type=int, default=[1,10], nargs=2)
parser.add_argument("-v", "--versuche", help="Anzahl der Versuche", type=int, default=5)
parser.set_defaults(func=zufallszahlen)
args = parser.parse_args()
args.func(args)