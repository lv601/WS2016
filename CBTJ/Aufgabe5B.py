from random import randint

def gluecksrad (versuche):
    zufallszahl = randint(1, 10)
    for i in range(versuche):
        eingabe = input("Geben Sie eine Zahl zwischen 1 und 10 ein: ")
        glueckszahl = eingabe
        if zufallszahl == int(glueckszahl):
            print ("Sie haben gewonnen!")
            break

        else:
            if i < (versuche-1):
                print ("Versuchen Sie es noch einmal!")

            else:
                print ("Leider nein")

    x = "Die richtige Zahl lautet: %s" % zufallszahl

    print (x)

gluecksrad(5)