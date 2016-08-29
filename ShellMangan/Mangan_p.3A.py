#Zahlenratespiel zw 1 und 10 mit random zahl und begrenzte anzahl von guesses
from random import randint
print("Welcome to the number guessing game! You have 5 guesses.")
r=randint(1, 10)
for guess in range(5):
    g=eval(input("Please guess a number between 1 and 10: "))
    if g == r:
        print("Correct!")
        break
    elif g>r:
        print("Wrong! You guessed too high!")
        continue
    elif g<r:
        print("Wrong! Your guessed too low!")
        continue
    else:
        print("I said between 1 and 10!")
        continue
print("End, thanks for playing!")
