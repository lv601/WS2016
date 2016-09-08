### Aufgabe 5b - Alexander Tolios - last modified am 06.09.2016 ; siehe Mitschrift vom 29.08.2016 ###

### Kopie von Aufgabe 3 - Alexander Tolios - last modified 06.09.2016 ; siehe Mitschrift vom 29.08.2016 ###

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


### ab hier neuer Code ###


from random import randint

def ratespiel(bereich, versuche):
    errate = randint(*bereich)
    
    for i in range(versuche):
        rate = input("Insert number between " + str(bereich[0]) + " and " + str(bereich[1]) + ": ")
        if bereich[0] > int(rate) or bereich[1] < int(rate):
            print("Bist angrennt? Du bist gesperrt!")
            break


        if rate == int(errate):
            print("Leiwi!")
            break
    
        if i == versuche - 1:
            print("You lost! You can't even guess ", errate, "!", sep="")
        elif i == versuche - 2:
            print("Last chance!")
        else:
            print(versuche - i - 1, "more guesses!")


ratespiel((0, 9), 5)

