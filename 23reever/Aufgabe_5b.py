from random import randint

def run_game(bereich, versuche):
    errate = randint(*bereich) # unpack tuple

    # Loops through all attempts
    for i in range(versuche):
        # Ask for input
        rate = input("Geben Sie eine Zahl zwischen " +
            str(bereich[0]) + " und " + str(bereich[1]) + " ein: ")

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

run_game((3, 7), 4)