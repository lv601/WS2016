from random import randint
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-v", "--versuche", type=int, help="Anzahl der maximalen Versuche")

args = parser.parse_args()

def ratespiel(versuche):

    zahl = randint(0, 10)  # eine Zufallszahl wird generiert
    for i in range(versuche):
        eingabezahl = input("Bitte geben Sie eine Zahl zwischen 0 und 10 ein:")
        if int(i+1 == versuche):
            print("Leider haben Sie die gesuchte Zahl nicht erraten können, es war die ", zahl)
            return None  # aus der Funktion kommt kein Rückgabewert
            break
        elif int(eingabezahl) > zahl:
            print("Die eingegebene Zahl ist größer als die gesuchte Zahl, probieren Sie es erneut")
            print("Sie haben noch", versuche - i-1, "Versuche")
            continue
        elif int(eingabezahl) < zahl:
            print("Die eingegebene Zahl ist kleiner als die gesuchte Zahl, probieren Sie es erneut")
            print("Sie haben noch", versuche - i-1, "Versuche")
            continue
        elif int(eingabezahl) == zahl:
            print("Juhu Sie haben die gesuchte Zahl gefunden")
            print("Sie haben", i+1, "Versuche gebraucht")
            return zahl #so kann die zu erratende Zahl später in einer Variable gespeichert werden
            break

return_wert = ratespiel(args.versuche)

print(return_wert)

