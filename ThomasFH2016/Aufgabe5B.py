from random import randint

antwort='J'

def rate_spass(minVal, maxVal, turns):
    randomTarget = randint(1, 10)
    print("Finden Sie die geheime Zahl (zwischen", minVal, "und", maxVal, ")")
    for i in range(0, turns):
        userInput = input("Geben Sie eine Zahl ein: ")
        if int(userInput) == randomTarget:
            print("Erwischt nach nur", i, "Versuch(en).")
            break
        elif int(userInput) > randomTarget:
            if turns-i-1 == 1:
                print("Zu hoch! - Letzter Versuch!")
                continue
            if maxVersuche - i - 1 == 0:
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

while antwort == 'J':
    rate_spass(1, 10, 3)
    antwort = input("Noch eine Runde (J/N)?")