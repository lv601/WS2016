from random import randint

def ratespiel():
    zufallszahl = randint(1, 10)
    wiederholungen = 5
    #user = input("Rate eine Zahl zwischen 1 und 10: ")

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

ratespiel()

# from random import randint
#
# def run_game(bereich, versuche):
#     errate = randint(*bereich) # unpack tuple
#
#     # Loops through all attempts
#     for i in range(versuche):
#         # Ask for input
#         rate = input("Geben Sie eine Zahl zwischen " +
#             str(bereich[0]) + " und " + str(bereich[1]) + " ein: ")
#
#         # guess right
#         if rate == str(errate):
#             print("Super! Sie haben die Zahl erraten.")
#             break # Leave loop - game finished
#
#         # No attempts left
#         if i == versuche - 1:
#             print("Sorry, Sie haben verloren. Die Zahl war ",
#                 errate, "!", sep="")
#         # Last attempt
#         elif i == versuche - 2:
#             print("Sie haben noch 1 Versuch")
#         # Next attempt
#         else:
#             print("Sie haben noch", versuche - i -1, "Versuche")
#
# run_game((3, 7), 4)