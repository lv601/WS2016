from random import randint

# Zufallszahl zwischen 1 und 10
errate = randint(1, 10)
versuche = 5

# Schleife über alle Versuche
for i in range(versuche):
    # Nach Zahl fragen - Input von User
    rate = input("Geben Sie eine Zahl zwischen 1 und 10 ein: ")

    # richtig
    if rate == str(errate):
        print("Super! Sie haben die Zahl erraten.")
        break # Leave loop - game finished

    # Keine Versuche mehr übrig (Zahl der Versuch = 5 siehe oben
    if i == versuche - 1:
        print("Sorry, Sie haben verloren. Die Zahl war ",
            errate, "!", sep="")

    # Letzter Versuch
    elif i == versuche - 2:
        print("Sie haben noch 1 Versuch")

    # Nächster Versuch
    else:
        print("Sie haben noch", versuche - i -1, "Versuche")