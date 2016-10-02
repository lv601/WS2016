import sys

def ausgabe (filename=None):
    h = "Hello World"
    if filename != None:
        d = open(filename, "w")

    else:
        d = sys.stdout

    d.write(h)


ausgabe()
ausgabe("ausgabe.txt")