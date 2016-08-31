from random import randint

upperBound = 10
guess = randint(1, upperBound)
tries = 3

guesses = []

for i in range(tries):
    rate = input("Enter number between (inclusive) 1 and 10:  ")

    if rate == str(guess):
        print("Great, got it")
        break
    else:
        try:
            rate = int(rate)
            if (rate > upperBound):
                print("enter a number between (inclusive) 1 and 10")

            if rate in guesses:
                print("dumb? tried this one already...")
                print("so far entered:")
                for k in range(0, len(guesses)):
                    print(guesses[k])

            guesses.append(rate)

        except ValueError:
            print("input error, enter int like string!")

        print("nope, tries left:", format(tries-i-1))

    if i == tries - 1:
        print("Sorry, lost")
