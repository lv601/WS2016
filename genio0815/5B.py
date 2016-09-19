from random import randint

def run_game(myRange, tries):

    target = randint(*myRange)
    guesses = []

    for i in range(tries):
        rate = input("Enter number between (inclusive) " + str(myRange[0]) + " and " + str(myRange[1]) + ":")

        try:
            rate = int(rate)
            if rate == target:
                print("Great, got it")
                # TIPP: Anstatt nur die Schleife zu verlassen, können Sie mit return
                # auch gleich die Funktion verlassen und auch gleich einen Rückgabewert
                # mitgeben. Z.B. bei Erfolg die erratete Zahl und bei nicht Erfolg None
                # zurückgeben. Somit können Sie den Rückgabewert der Funktion in andern
                # Funktionen mitverabrbeiten, wenn gewünscht.
                #    return zufallszahl
                #    return None # in Zeile 43
                break
            else:

                if (rate > myRange[1]):
                    print("enter a number between (inclusive) 1 and %i:  " % myRange[1])

                # TIPP: Wenn Sie fehlerhafte oder doppelte Eingaben abfragen wollen, dürfen
                # Sie bei einer falschen Eingabe den Zähler nicht weiterlaufen lassen. Sonst
                # verliert der Spieler einen Versuch. Sie können die Abfrage noch zusätzlich
                # in eine while Schleife packen, die solange läuft bis eine valide Eingabe
                # erfolgt.
                if rate in guesses:
                    print("dumb? tried this one already...")
                    print("integers entered so far :")
                    for k in range(0, len(guesses)):
                        print(guesses[k])

                guesses.append(rate)

        except ValueError:
            print("input error, enter int like string!")

        print("nope, tries left:", format(tries-i-1))

        # TIPP: Anstatt die letzte Iteration zu prüfen, können Sie auch den
        # 'else'-Zweig der for Schleife verwenden. Vorteil weniger Abfragen und
        # übersichtlicher
        # else:
        #   print("Sorry, lost")
        if i == tries - 1:
            print("Sorry, lost")

run_game((1, 15), 3)