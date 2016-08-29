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
