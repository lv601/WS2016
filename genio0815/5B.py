from random import randint

def run_game(myRange, tries):

    target = randint(*myRange)
    guesses = []

    for i in range(tries):
        rate = input("Enter number between (inclusive) " + str(myRange[0]) + " and " + str(myRange[1]) + ":")

        try:
            rate = int(rate)
            if rate == target:
                return
            else:

                if (rate > myRange[1]):
                    print("enter a number between (inclusive) 1 and %i:  " % myRange[1])

                    # TIPP: Wenn Sie fehlerhafte oder doppelte Eingaben abfragen wollen, dürfen
                    # Sie bei einer falschen Eingabe den Zähler nicht weiterlaufen lassen. Sonst
                    # verliert der Spieler einen Versuch. Sie können die Abfrage noch zusätzlich
                    # in eine while Schleife packen, die solange läuft bis eine valide Eingabe
                    # erfolgt. => it was intended that the wrong inputs do increase the counter!

                if rate in guesses:
                    print("dumb? tried this one already...")
                    print("integers entered so far :")
                    for k in range(0, len(guesses)):
                        print(guesses[k])

                guesses.append(rate)

        except ValueError:
            print("input error, enter int like string!")

        print("nope, tries left:", format(tries-i-1))

    else:
       print("Sorry, lost")

    return


run_game((1, 15), 3)