from random import randint
from argparse import ArgumentParser


def run_game(args):

    errate = randint(*args.range)

    for i in range(args.range):

        rate = int(input("Geben Sie eine Zahl zwischen {0} un {1} ein: ".format(*args.range)))

        if rate == errate:
            print ("Super! Sie haben die Zahl erraten.")
            return errate
        elif rate < errate:
            print("Zu niedrig!")
        elif rate > errate:
            print("Zu hoch!")
    else:
            print ("Sorry, Sie haben verloren. Versuchen Sie es noch einmal!")

parser = ArgumentParser()

parser.add_argument("-r", "--range", help="Number range. [from to]", type=int, default=[1,9], nargs=2)
parser.set_defaults(func=run_game)

args = parser.parse_args()



