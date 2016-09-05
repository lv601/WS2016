import random

zahl = random.randint(1, 10)
print ("Raten Sie eine Zahl zwischen 1 und 10")
print ("Sie koennen 5 mal versuchen")

for i in range (1, 6):
    eingabe = input ("eraten Sie eine Zahl: ")

    if eingabe == zahl:
        print ("Sie haben die Zahl eraten!")
        break
    else:
        print ("Das ist nicht die richtige Zahl")

if eingabe ==zahl:
        print ("Sie haben die Zahl eraten!")
else:
    print ("Das Spiel wird beebdet")

