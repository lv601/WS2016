from random import randint

# mit Hilfe von randit() eine Zufallszahl zw. 1 und 10
zufallszahl = randint(1, 10)
wiederholungen = 5

# for schleife über alle Versuche
for i in range(wiederholungen):

    # Nach Zahl fragen - Input von User
    user = input("Rate eine Zahl zwischen 1 und 10: ")

    # 1. Fall: Antwort von user ist richtig
    if  user == str(zufallszahl):
        print("Gratuliere! Die Zahl ist richtig.")
        # schleife wird beendet
        break

    # 2a Fall: Zahl war zu hoch:
    if user > str(zufallszahl):
        print("Die Zahl ist zu hoch. Du hast noch", wiederholungen - i -1, "Vesuche.")

    # 2b Fall: Zahl war zu niedrig:
    if user < str(zufallszahl):
        print("Die Zahl ist zu niedrig. Du hast noch", wiederholungen - i -1, "Vesuche.")

    # 3. Fall Zahl wird nicht erraten
    if i == wiederholungen - 1:
        print("Du hast leider verloren. Die gesuchte Zahl ist: ", zufallszahl, "!")
        break







    # # Keine Versuche mehr übrig (Zahl der Versuch = 5 siehe oben
    # if i == versuche - 1:
    #     print("Sorry, Sie haben verloren. Die Zahl war ",
    #         errate, "!", sep="")
    #
    # # Letzter Versuch
    # elif i == versuche - 2:
    #     print("Sie haben noch 1 Versuch")
    #
    # # Nächster Versuch
    # else:
    #     print("Sie haben noch", versuche - i -1, "Versuche")