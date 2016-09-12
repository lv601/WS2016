from random import randint
def ratespiel(Bereich, v1):
    rate = randint(*Bereich)
    for i in range(v1):
        errate = input("Gib eine nummer zwischen " + str(Bereich[0]) + " und " + str(Bereich[1]) + " ein:")
        if errate == int(rate):
            print("Richtig Haberer!")
        else:
            print("Leider nein.")