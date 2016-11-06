print("Zahlratenspiel\n")

from random import randint

ran = randint(1,10)

for i in range(5):
    eingabe = int(input("Geben Sie eine Zahl zwischen 1 und 10 an:"))

    if ran == eingabe:
        print("Sehr gut, Sie haben die Zahl erraten!")
        print("Die erzeugte Zufallszahl war: ", ran)
        break

    elif ran < eingabe:
        print("Die Zahl ist zu hoch!")

    else:
        print("Die Zahl ist zu niedrig!")

    if i == 4:
        print("Ouch, Sie haben keine Versuche mehr!")
        print("Der erzeugte Zufallszahl war: ", ran)
        break

    print("Sie haben noch ", 4 - i, " Versuche!")