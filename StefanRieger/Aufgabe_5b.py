from random import randint
def ratespiel(Bereich, v1):
    rate = randint(*Bereich)
    # TIPP: Hier können Sie den 'else' Zweig der for Schleife verwenden um noch
    # eine game over Meldung zu schreiben
    for i in range(v1):
        errate = input("Gib eine nummer zwischen " + str(Bereich[0]) + " und " + str(Bereich[1]) + " ein:")
        if errate == int(rate):
            # ACHTUNG: Hier brauchen Sie die 'break' Anweisung sonst wird die Schleife nicht verlassen
            print("Richtig Haberer!")
        else:
            print("Leider nein.")