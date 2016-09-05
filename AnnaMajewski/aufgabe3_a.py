## Date: 04.09.2016
## Author: Anna Majewski
## Description: Zahlenratespiel

from random import randint
# Importieren von randint aus random

zahl = randint(1,10)
# Zufallszahl wird generiert
anzahl = 5
# Anzahl der Würfe

print("Willkommen beim Ratespiel. Erraten Sie eine Zahl zwischen 1 und 10!")

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

