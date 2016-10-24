import sys

def welt(filename=None):
    if filename:
        f = open(filename, "w")
    else:
        f = sys.stdout

    f.write("Hello World")

welt()
welt("adsf.txt")