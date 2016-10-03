#! /usr/bin/python3

from random import randint
from argparse import ArgumentParser as aP

parser = aP(prog='Integer guesser', description="little game; lets the user guess an integer number "
                                                "between to prior entered bounds", usage='enter integer numbers for '
                                                                                         'lower and upper bound and '
                                                                                         'the number of possible '
                                                                                         'guesses')

parser.add_argument("-l", "--lowerbound", dest="lB", type=int, default="0", help="lower bound (def. 0)")
parser.add_argument("-u", "--upperbound", dest="uB", type=int, default="10", help="lower bound (def. 10)")
parser.add_argument("-g", "--guesses", dest="tries", type=int, default="3", help="number of guesses (def. 3)")

args = parser.parse_args()

myRange = (args.lB, args.uB)

target = randint(*myRange)
guesses = []

for i in range(args.tries):
    rate = input("\tEnter number between (inclusive) " + str(myRange[0]) + " and " + str(myRange[1]) + ":")

    try:
        rate = int(rate)
        if rate == target:
            print("\tjope, correct...done")
            exit(0)
        else:

            if ((rate < myRange[0]) or (rate > myRange[1])):
                print("\tseems not so easy...enter a number between (inclusive) {} and {}".format(myRange[0],
                                                                                                  myRange[1]))

            if rate in guesses:
                print("\tdumb? tried this one already...")
                print("\tintegers entered so far :")
                for k in range(0, len(guesses)):
                    print("\t" + guesses[k])

            guesses.append(rate)

    except ValueError:
        print("\tinput error, enter int like string!")

    print("\tnope, tries left:", format(args.tries-i-1))

else:
    print("\tSorry, lost")

exit(0)



