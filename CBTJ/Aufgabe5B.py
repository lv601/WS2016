from random import randint

def gluecksrad(versuche):
    zufallszahl = randint(1, 10)
    for i in range(versuche):
        eingabe = input("Geben Sie eine Zahl zwischen 1 und 10 ein: ")
        glueckszahl = eingabe
        if zufallszahl == int(glueckszahl):
            print ("Sie haben gewonnen!")
            # TIPP: Statt nur die Schleife zu verlassen, könnten Sie gleich auch
            # Funktion verlassen und einen Rückgabewert definieren.
            # return zufallszahl
            # return None  # Zeile 24
            break

        else:
            if i < (versuche-1):
                print ("Versuchen Sie es noch einmal!")

            else:
                # TIPP: Dafür können Sie auch den 'else' Zweig der for Schleife
                # nutzen, der nur durchlaufen wird, wenn die Schleife komplett
                # durch gelaufen ist.
                print ("Leider nein")

    # TIPP: Das können sie einfach direkt printen anstatt eine sonst unnütze
    # Variable zu generieren.
    # Vergeben sie sprechende Namen. Bei x denke ich eher an Koordinaten ala
    # (x,y). Das hilft bei größeren Projekten, die übersicht zu halten
    # print("Die richtige Zahl lautet: {}".format(zufallszahl))
    x = "Die richtige Zahl lautet: %s" % zufallszahl

    print(x)

gluecksrad(5)
