from random import randint

antwort='J'

def rate_spass(minVal, maxVal, turns):
    # ACHTUNG: Sie fragen minVal und maxVal zwar ab, aber verwenden sie nicht
    randomTarget = randint(1, 10)
    print("Finden Sie die geheime Zahl (zwischen", minVal, "und", maxVal, ")")
    for i in range(0, turns):
        userInput = input("Geben Sie eine Zahl ein: ")
        if int(userInput) == randomTarget:
            print("Erwischt nach nur", i, "Versuch(en).")
            # TIPP: Anstatt nur die Schleife zu verlassen, können Sie mit return
            # auch gleich die Funktion verlassen und auch gleich einen Rückgabewert
            # mitgeben. Z.B. bei Erfolg die erratete Zahl und bei nicht Erfolg None
            # zurückgeben. Somit können Sie den Rückgabewert der Funktion in andern
            # Funktionen mitverabrbeiten, wenn gewünscht.
            #    return zufallszahl
            #    return None # in Zeile 41
            break
        elif int(userInput) > randomTarget:
            if turns-i-1 == 1:
                print("Zu hoch! - Letzter Versuch!")
                continue
            if maxVal - i - 1 == 0:
                print("Zu hoch! - Keine Versuche mehr übrig")
                continue
            else:
                print("Zu hoch! - Noch", turns-i-1, "Versuch(e).")
        elif int(userInput) < randomTarget:
            if turns - i - 1 == 1:
                print("Zu niedrig! - Letzter Versuch!")
                continue
            if turns - i - 1 == 0:
                print("Zu niedrig! - Keine Versuche mehr übrig")
                continue
            else:
                print("Zu niedrig! - Noch", turns-i-1, "Versuch(e).")
    else:
        print("Leider nicht erraten. Die Zahl war:", randomTarget)

# Tipp: verwenden Sie antwort.upper() == 'J'. Dann funktioniert j und J als Antwort
while antwort == 'J':
    rate_spass(1, 10, 3)
    antwort = input("Noch eine Runde (J/N)? ")