from random import randint
maxVersuche = 5
antwort='J'

while antwort == 'J':
    zufallsZahl = randint(1, 10)
    for i in range(0,maxVersuche):
        eingabe=input('Rate die Zahl zwischen 1 und 10: ')
        if int(eingabe) == int(zufallsZahl):
            print("Erwischt nach nur", i, "Versuch(en).")
            break
        elif int(eingabe) > int(zufallsZahl):
            if maxVersuche-i-1 == 1:
                print("Zu hoch! - Letzter Versuch!")
                continue
            if maxVersuche - i - 1 == 0:
                print("Zu hoch! - Keine Versuche mehr übrig")
                continue
            else:
                print("Zu hoch! - Noch", maxVersuche-i-1, "Versuch(e).")
        elif int(eingabe) < int(zufallsZahl):
            if maxVersuche - i - 1 == 1:
                print("Zu niedrig! - Letzter Versuch!")
                continue
            if maxVersuche - i - 1 == 0:
                print("Zu niedrig! - Keine Versuche mehr übrig")
                continue
            else:
                print("Zu niedrig! - Noch", maxVersuche-i-1, "Versuch(e).")
    else:
        print("Leider nicht erraten. Die Zahl war:", zufallsZahl)
    antwort=input("Noch eine Runde (J/N)?")
