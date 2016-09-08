### Aufgabe 3a - Alexander Tolios - last modified 06.09.2016 ; siehe Mitschrift vom 29.08.2016 ###

### Lösung von mir

from random import randint


i = 0
wahrezahl = randint(1, 10)

while i <= 4:

    eingabe = input("Bitte Zahl eingeben: ")
    eingabe = int(eingabe)

    if eingabe == wahrezahl:
        print("Juchee!")
        break
    elif eingabe < wahrezahl:
        print("You're too low")
    else: 
        print("You're too high")

    if i < 4:
        print("Try again!")
    elif i == 4:
        print("Letzter Versuch!") # Lieber Herr Auer, das Ratespiel an sich funktioniert, aber die Warnung beim letzten Versuch nicht. Any ideas?
    else:
        break
    i += 1
else:
    print("You tried", i, "times and you really suck at guessing!")





### Dies ist die Lösung von Aufgabe 3a von nauer

from random import randint

# Get a random number between 1 and 10
errate = randint(1, 10)
versuche = 5

# Loops through all attempts
for i in range(versuche):
    # Ask for input
    rate = input("Geben Sie eine Zahl zwischen 1 und 10 ein: ")

    # guess right
    if rate == str(errate):
        print("Super! Sie haben die Zahl erraten.")
        break # Leave loop - game finished

    # No attempts left
    if i == versuche - 1:
        print("Sorry, Sie haben verloren. Die Zahl war ",
            errate, "!", sep="")
    # Last attempt
    elif i == versuche - 2:
        print("Sie haben noch 1 Versuch")
    # Next attempt
    else:
print("Sie haben noch", versuche - i -1, "Versuche")


