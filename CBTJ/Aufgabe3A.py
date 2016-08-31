from random import randint

zufallszahl = randint (1,10)




for i in range(5):
    glueckszahl1 = input("Geben Sie eine Zahl zwischen 1 und 10 ein: ")
    if zufallszahl == int(glueckszahl1):
        print ("Sie haben gewonnen!")
        break

    else: print ("Versuchen Sie es noch einmal!")

x = "Die richtige Zahl lautet: %s" % zufallszahl

print (x)
