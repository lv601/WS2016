print("Zahlratenspiel\n")

from random import randint

def randomgame(bereich, versuche):
    ran = randint(*bereich)

    for i in range(versuche):
        eingabe = int(input("Geben Sie eine Zahl zwischen " + str(bereich[0]) + " und " + str(bereich[1]) + " an:"))

        if ran == eingabe:
            print("Sehr gut, Sie haben die Zahl erraten!")
            print("Der erzeugte Zufallszahl war: ", ran)
            # TIPP: Anstatt nur die Schleife zu verlassen, können Sie mit return
            # auch gleich die Funktion verlassen und auch gleich einen Rückgabewert
            # mitgeben. Z.B. bei Erfolg die erratete Zahl und bei nicht Erfolg None
            # zurückgeben. Somit können Sie den Rückgabewert der Funktion in andern
            # Funktionen mitverabrbeiten, wenn gewünscht.
            #    return zufallszahl
            #    return None # in Zeile 38
            break

        elif ran < eingabe:
            print("Die Zahl ist zu hoch!")

        else:
            print("Die Zahl ist zu niedrig!")

        # TIPP: Anstatt die letzte Iteration zu prüfen, können Sie auch den
        # 'else'-Zweig der for Schleife verwenden. Vorteil weniger Abfragen und
        # übersichtlicher
        # else:
        #   print("Ouch, Sie haben keine Versuche mehr!")
        #   print("Die erzeugte Zufallszahl war: ", ran)
        if i == versuche-1:
            print("Ouch, Sie haben keine Versuche mehr!")
            print("Die erzeugte Zufallszahl war: ", ran)
            break

        print("Sie haben noch ", versuche-i-1, " Versuche!")

randomgame((1,10),5)

# Example with return value
# if randomgame((1,10),5)
#     print("Game Over")
# else:
#     run_next_game()