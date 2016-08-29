from random import randint

right = False
guessCount = 0
randomNum = randint(1,10)
print("Geben Sie eine Zahl zwischen 1 und 10 ein: ", end = "")
while right == False:
    guess = int(input())
    guessCount += 1
    if guess in range(1,11):
        if guess == randomNum:
            print("Richtige Zahl! Sie haben gewonnen.")
            right = True
        elif guess > randomNum:
            print("Zahl zu gross.")
        elif guess < randomNum:
            print("Zahl zu klein.")
    else:
        print("Die Zahl muss zwischen 1 und 10 sein.")
    if guessCount == 5 and right == False:
        print("Sie haben verloren.")
    else:
        print("Sie haben noch {} Versuche. Neuer Versuch: ".format(5 - guessCount), end = "")
