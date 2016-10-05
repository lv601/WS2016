#!/usr/bin/env python3

from random import randint
from argparse import ArgumentParser


def run_game(args):
    errate = randint(*args.range) # unpack tuple

    # Loops through all attempts
    for i in range(args.tries):
        # Ask for input
        rate = int(input("Geben Sie eine Zahl zwischen {0} un {1} ein: ".format(*args.range)))

        # guess right
        if rate == errate:
            print("Super! Sie haben die Zahl erraten.")
            return errate
        elif rate < errate:
            print("Zu niedrig!")
        else:
            print("Zu hoch!")

        # Last attempt
        if args.tries - 1 > i >= 0:
            if i == args.tries - 2:
                print("Sie haben noch 1 Versuch")
            # Next attempt
            else:
                print("Sie haben noch {} Versuche".format(args.tries - i - 1))
    else:
        # No attempts left
        print("Sorry, Sie haben verloren. Die Zahl war {}!".format(errate))
        return None


parser = ArgumentParser()

parser.add_argument("-r", "--range", help="Number range. [from to]", type=int, default=[1, 9], nargs=2)
parser.add_argument("-t", "--tries", help="How many tries", type=int, default=5)
parser.set_defaults(func=run_game)

args = parser.parse_args()


while args.func(args):
   print("\nSehr gut! Gleich das nächste Spiel aber ein bisschen schwieriger.\n")
   args.range[1] += 1
else:
   print("\nGame Over\n")