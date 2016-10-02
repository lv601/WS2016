from random import randint
import time
zahl = randint(1,10)

for i in range(5):
    auswahl = input('Wähle eine Zahl zwischen 1 und 10:  ')
    auswahl = int(auswahl)
    if auswahl == zahl:
        print ('richtig')
        break
    elif auswahl < zahl:
        print ('zu niedrig!')
        time.sleep(1)
        
    elif auswahl > zahl:
        print ('zu hoch!')
        time.sleep(1)
        

else:
    print ('game over')
        
