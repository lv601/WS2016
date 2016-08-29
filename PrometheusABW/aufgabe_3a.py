#Zahlenratespiel
import random

print("Zahlenraten 0-50")
counter = 2
zahl = random.randint(0,50)
#print(zahl)
while counter >= 0:
    userin = int(input("give me a number:  "))
    if userin == zahl:
        print("well done")
        counter = -1
    else:
        print("sorry man")
        counter -= 1

