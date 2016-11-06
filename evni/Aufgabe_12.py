from argparse import ArgumentParser
from random import randint
import time

parser = ArgumentParser()
parser.add_argument('-v', '--versuche', type=int, help='Anzahl der Versuche')
args = parser.parse_args()

def game(versuche):
    zahl = randint(1,10)
    versuche = 5

    for i in range(versuche):
        auswahl = input('Wähle eine Zahl zwischen 1 und 10 :  ')
        if auswahl == str(zahl):
            print ('richtig')
            break
        if auswahl < str(zahl):
            print ('zu niedrig!')
            time.sleep(1)

        if auswahl > str(zahl):
            print ('zu hoch!')
            time.sleep(1)

        if i == versuche -1:
            print ('game over')


ergebnis=game(args.versuche)
print(ergebnis)
