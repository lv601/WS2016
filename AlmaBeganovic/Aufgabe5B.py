from random import randint

def run_game(bereich, versuche):
    errate = randint(*bereich)


    for i in range(versuche):

        rate = int(input("Geben Sie eine Zahl zwischen {0} un {1} ein: ".format(*bereich)))


        if rate == errate:
            print("Bravo! Sie haben die Zahl erraten.")
            return errate
        elif rate < errate:
            print("Zahl zu niedrig!")
        else:
            print("Zahl zu hoch!")


        if versuche - 1 > i >= 0:
            if i == versuche - 2:
                print("Sie haben noch 1 Versuch")
            #
            else:
                print("Sie haben noch {} Versuche".format(versuche - i - 1))
    else:

        print("Sorry, Sie haben verloren. Die Zahl war {}!".format(errate))
        return None

