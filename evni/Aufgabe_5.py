#Funktionen erstellen für Aufgabe 2,3A,3B#

########Aufgabe2#######
from pprint import pprint

def add_adressbuch(adressbuch, **neu):
    adressbuch.append(dict(**neu))
adressbuch =[]

add_adressbuch(adressbuch, vorname='max', nachname='mustermann',hobbies=('schwimmen','tanzen','lesen'), alter='43',
              eigenschaften=({'geschicklichkeit':'10', 'IQ':'98', 'gewicht':'83', 'haarfarbe':'blond'}),
              geschlecht='männlich')
#pprint(adressbuch)
add_adressbuch(adressbuch, studium='medizin')

pprint(adressbuch)


########Aufgabe3A######
from random import randint
import time

def game():
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
game()

########Aufgabe3B######
def codon():
    sequenz = input('Geben sie die Sequenz ein: ')
#print (sequenz)
    drei = 3
    for i in range(0, len(sequenz) - drei+1):
        print(' '*i, sequenz[i:i+drei])
codon()
   
