import random #Importiert das Modul "random"


from random import randint #die Funktion "randint" wird importiert

def ratespiel(versuche):

    zahl = randint(0, 10)  # eine Zufallszahl wird generiert
    for i in range(versuche):
        eingabezahl = input("Bitte geben Sie eine Zahl zwischen 0 und 10 ein:")
        #eingabezahl = int(eingabezahl)
        if int(eingabezahl) > zahl:
            print("Die eingegebene Zahl ist größer als die gesuchte Zahl, probieren Sie es erneut")
            print("Sie haben noch", versuche - i-1, "Versuche")
            continue
        elif int(eingabezahl) < zahl:
            print("Die eingegebene Zahl ist kleiner als die gesuchte Zahl, probieren Sie es erneut")
            print("Sie haben noch", versuche - i-1, "Versuche")
            continue
        elif int(eingabezahl) == zahl:
            print("Juhu Sie haben die gesuchte Zahl gefunden")
            print("Sie haben", i+1, "Versuche gebraucht")
            break
        else:
            print("Leider haben Sie die gesuchte Zahl nicht erraten können, es war die ", zahl)
            break

eingabe = int(input("Wie oft wollen Sie raten?"))
ratespiel(eingabe)