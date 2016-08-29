from random import randint

ergebnis = randint(1,10)

print ("Sie haben 3 Versuche eine Zahl zu erraten!")
for i in range(3):
    raten = input("Geben Sie eine Zahl zwischen 1 und 10 ein")
    raten = int(raten)
    if raten == ergebnis:
        print ("Richtig! Die Zahl war", raten)
        break
    elif raten < ergebnis:
        print ("Die Zahl ist größer als", raten, "!")
    elif raten > ergebnis:
        print ("Die Zahl ist kleiner als", raten, "!")
else:
    print ("Sie haben die Zahl leider nicht erraten.")
