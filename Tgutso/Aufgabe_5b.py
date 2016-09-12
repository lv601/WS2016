print("Zahlratenspiel\n")

from random import randint

def randomgame(bereich, versuche):
    ran = randint(*bereich)

    for i in range(versuche):
        eingabe = int(input("Geben Sie eine Zahl zwischen " + str(bereich[0]) + " und " + str(bereich[1]) + " an:"))

        if ran == eingabe:
            print("Sehr gut, Sie haben die Zahl erraten!")
            print("Der erzeugte Zufallszahl war: ", ran)
            break

        elif ran < eingabe:
            print("Die Zahl ist zu hoch!")

        else:
            print("Die Zahl ist zu niedrig!")

        if i == versuche-1:
            print("Ouch, Sie haben keine Versuche mehr!")
            print("Die erzeugte Zufallszahl war: ", ran)
            break

        print("Sie haben noch ", versuche-i-1, " Versuche!")

randomgame((1,10),5)