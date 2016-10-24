from random import randint

# ACHTUNG: In ihren Beispielen sind viele Vertipper und auch falsche Einzüge.
# Ich vermute sie verwenden einen gewöhnlichen Texteditor. Benutzen Sie besser
# eine Python IDE wie pyCharm oder Spyder
def run_game(bereich, versuche):
    errate=randint(*bereich)
    for i in range(versuche):
        rate=input("Guess a number between "+str(bereich[0])+" and "+str(bereich[1])+" : ")
        if rate==str(errate):
            print("Correct!")
            break
        else:
            print("Wrong!")
            # ACHTUNG: break verlässt die Schleife komplett keine Möglichkeit in die nächste Runde zu kommen
            # Verwenden Sie continue
            break


run_game((1,5),5)
