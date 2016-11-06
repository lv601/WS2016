### Aufgabe 10 - Alexander Tolios - last modified am 29.10.2016 ###

import sys

def func(filename=None):
    if filename:
        f = open(filename, "w")
    else:
        f = sys.stdout
    # Makes program independent from stream origin
    f.write("Hello World")

# Run
func()
func("Ausgabe.txt")
