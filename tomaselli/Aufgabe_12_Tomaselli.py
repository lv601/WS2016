from random import randint
from argparse import ArgumentParser

def random(args):
    x = int(input("zahl zw dem bereich {0} un {1} eingeben: ".format(*args.bereich)))
    y = randint(*args.bereich)
        
    c = 1
        
    while c < args.anzahl:

        if x == y:
            print('welldone')
            print(y)
            break

        elif x != y:
            if x > int(args.bereich[1]):
                x = int(input("ihre zahl war auserhalb des bereiches. zahl zw dem bereich {0} un {1} eingeben: ".format(*args.bereich)))
                c = c + 1
                continue
            elif x < int(args.bereich[0]):
                x = int(input("ihre zahl war auserhalb des bereiches. zahl zw dem bereich {0} un {1} eingeben: ".format(*args.bereich)))
                c = c + 1
                continue

            else:
                x = int(input("zahl zw dem bereich {0} un {1} eingeben: ".format(*args.bereich)))
                c = c + 1
                continue

        else:
            print(x,y)

    if c == args.anzahl:
        if x == y:
            print('welldone')
            print(y)
        else:
            print('sorry! sie haben leider verloren', 'die zahl war: ', y)


parser = ArgumentParser()

parser.add_argument("-r", "--bereich", help="bereich", type=int, default=[1, 7], nargs=2)
parser.add_argument("-t", "--anzahl", help="anzahl versuche", type=int, default=5)
parser.set_defaults(func=random)

args = parser.parse_args()
args.func(args)