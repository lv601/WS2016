from random import randint

def guessing_game(guesses, num1, num2):
    random_num = randint(num1, num2)
    print("Geben Sie eine Zahl zwischen {} und {} ein: ".format(num1, num2), end="")

    for guess_count in range(num1, num2):
        guess = int(input())
        guess_count -= 1

        if guess in range(num1, num2 + 1):
            if guess == random_num:
                print("Richtige Zahl! Sie haben gewonnen.")
                win = True
                break
            elif guess > random_num:
                print("Zahl zu gross.")
            elif guess < random_num:
                print("Zahl zu klein.")
        else:
            print("Die Zahl muss zwischen 1 und 10 liegen.")

        if guess_count == 0:
            print("Sie haben verloren.")
            win = False
        elif guess_count > 0:
            print("Sie haben noch {} Versuche. Neuer Versuch: ".format(guesses - guess_count), end="")

        return win

guessing_game(5, 1, 3)
