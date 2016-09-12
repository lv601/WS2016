#Zahlenratespiel

from random import randint
richtig = randint(1, 10)
chancen = 5
for i in range(chancen):
    rate = input("Gib eine Zahl zwischen 1 und 10 ein:")
    rate = int(rate)
    if rate < richtig:
        print("Zu niedrig!")
    elif rate > richtig:
        print("Zu hoch!")
    elif rate == richtig:
        print("Erraten, du Held!")
        break
    if i == chancen-1:
        print("Verloren, du Versager! Die richtige Zahl wäre ", rate, " gewesen!", sep="")
    elif i == chancen-2:
        print("Letzter Versuch, bemüh dich!")
    else:
        print("Du hast noch", versuche-i-1, "Versuche")