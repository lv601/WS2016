from random import randint


def guessing_game(guesses, num1, num2):
    right = False
    guess_count = guesses
    random_num = randint(num1, num2)
    print("Geben Sie eine Zahl zwischen {} und {} ein: "
          .format(num1, num2), end="")

    # TIPP; hier eignet sich eine for Schleife besser, dann können Sie auch
    # 'guess_cout' verzichten
    #
    # for guess_count in range(num1, num2):
    while right is False:
        guess = int(input())
        guess_count -= 1
        if guess in range(num1, num2 + 1):
            if guess == random_num:
                print("Richtige Zahl! Sie haben gewonnen.")
                right = True
            elif guess > random_num:
                print("Zahl zu gross.")
            elif guess < random_num:
                print("Zahl zu klein.")
        else:
            print("Die Zahl muss zwischen 1 und 10 sein.")

        # TIPP: Hier könnten Sie auch den 'else'-Zweig der while Schleife
        # benutzen, der nur aufgerufen wird, wenn die Schleife normal beendet
        # wird (ohne break)
        # else:
        #     print("Sie haben verloren.")
        if guess_count == 0 and right is False:
            print("Sie haben verloren.")
        elif guess_count > 0 and right is False:
            guess_left = guesses - guess_count
            print("Sie haben noch {} Versuche. Neuer Versuch: "
                  .format(guess_left), end="")

guessing_game(5, 1, 3)

# TIPP: weiters könnten sie noch einen Rückgabewert definieren, damit z.B. die
# aufrufende Funktion mitbekommt, ob das Spiel erfolgreich beendet wurde oder
# nicht
