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
                break
            else:

                if (rate > myRange[1]):
                    print("enter a number between (inclusive) 1 and %i:  " % upperBound)

                if rate in guesses:
                    print("dumb? tried this one already...")
                    print("integers entered so far :")
                    for k in range(0, len(guesses)):
                        print(guesses[k])

                guesses.append(rate)

        except ValueError:
            print("input error, enter int like string!")

        print("nope, tries left:", format(tries-i-1))

        if i == tries - 1:
            print("Sorry, lost")

run_game((1, 15), 3)