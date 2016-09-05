## Date: 04.09.2016
## Author: Anna Majewski
## Description: Ratespiel so umschreiben, damit es eine Funktion ist.

# Zuerst Ratespiel hinüberkopieren.
# Ich könnte import nutzen, ABER ich will aus der anderen Datei
# nicht alle prints entfernen, damit sie ausführbar bleibt.

from random import randint
# Importieren von randint aus random

def guess_game(min, max, guesses):
# min und max bestimmen die Range der zufälligen Zahl
# guesses bestimmt die Anzahl der Versuche.
    zahl = randint(min,max)
    # Zufallszahl wird generiert
    anzahl = guesses
    # Anzahl der Würfe

    print("Willkommen beim Ratespiel. Erraten Sie eine Zahl zwischen", min, "und", max, "!")

    for index, x in enumerate(range(anzahl)):
        eingabe = input("Geben Sie Ihre Zahl ein:")
    # Eingabe wird direkt in einer Variable gespeichert.
        eingabe = int(eingabe)
    # Die Zahl wird von einem String zu einem Integer umgewandelt.
        if eingabe == zahl:
            print("SUPER! Sie haben die Zahl erraten!")
            break
        elif eingabe < zahl:
            print("Zu niedrig. Die Zahl ist größer!", "Sie haben noch", anzahl-1-index, "Versuche!")
        elif eingabe > zahl:
            print("Zu hoch. Die Zahl ist kleiner!", "Sie haben noch", anzahl-1-index, "Versuche!")

guess_game(1, 8, 2)
