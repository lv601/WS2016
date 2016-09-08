# coding=utf-8
from random import randint

def run_game(bereich):
    zufazahl = randint(1, bereich)
    return zufazahl

bereich = input ("Definieren Sie den Bereich für die Zufallszahl zwischen 1 und n ein: ")

versuche = input ("Bitte geben Sie Anzahl von Versuchen ein: ")

print ("Bereich ist zwischen 1 und ", bereich)
print ("Anzahl von Versuchen ist ", versuche)

zufal_global = run_game(bereich)
#print (zufal_global)

for i in range (1, versuche+1):
    zahl = input("Bitte geben Sie eine Zahl aus dem Bereich: ")
    if zahl == zufal_global:
        print ("Zahl ist erraten", zufal_global)
        break;

    if zahl < zufal_global:
        print ("Zahl ist kleiner als Zufallszahl")

    if zahl > zufal_global:
        print ("Zahl ist grosser als Zufallszahl")