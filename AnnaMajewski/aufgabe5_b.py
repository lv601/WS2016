## Date: 04.09.2016
## Author: Anna Majewski
## Description: Ratespiel so umschreiben, damit es eine Funktion ist.

# Zuerst Ratespiel hinüberkopieren.
# Ich könnte import nutzen, ABER ich will aus der anderen Datei
# nicht alle prints entfernen, damit sie ausführbar bleibt.

from random import randint
# Importieren von randint aus random

def guess_game(min, max, guesses):
    """number guess game in range from 'min' to 'max', with 'guesses' guesses"""
# min und max bestimmen die Range der zufälligen Zahl
# guesses bestimmt die Anzahl der Versuche.
    zahl = randint(min,max)
    # Zufallszahl wird generiert
    anzahl = guesses
    # Anzahl der Würfe

    print("Willkommen beim Ratespiel. Erraten Sie eine Zahl zwischen", min, "und", max, "!")

    # TIPP: Hier können Sie den 'else'-Zweig der for Schleife verwenden, um noch eine game_over
    # Nachricht zu schicken
    # else:
    #   print("Du hast leider verloren.")

    # TIPP: enumerate können Sie sich hier sparen, da index hier
    # gleich x ist
    # for index range(anzahl):
    for index, x in enumerate(range(anzahl)):
        eingabe = input("Geben Sie Ihre Zahl ein:")
    # Eingabe wird direkt in einer Variable gespeichert.
        eingabe = int(eingabe)
    # Die Zahl wird von einem String zu einem Integer umgewandelt.
        if eingabe == zahl:
            print("SUPER! Sie haben die Zahl erraten!")
            # TIPP: Anstatt nur die Schleife zu verlassen, können Sie mit return
            # auch gleich die Funktion verlassen und auch gleich einen Rückgabewert
            # mitgeben. Z.B. bei Erfolg die erratete Zahl und bei nicht Erfolg None
            # zurückgeben. Somit können Sie den Rückgabewert der Funktion in andern
            # Funktionen mitverabrbeiten, wenn gewünscht.
            #    return zahl
            break
        elif eingabe < zahl:
            print("Zu niedrig. Die Zahl ist größer!", "Sie haben noch", anzahl-1-index, "Versuche!")
        elif eingabe > zahl:
            print("Zu hoch. Die Zahl ist kleiner!", "Sie haben noch", anzahl-1-index, "Versuche!")

guess_game(1, 8, 2)
