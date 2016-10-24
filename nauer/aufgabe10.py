#!/usr/bin/env python3

""" Aufgabe 10
Schreiben Sie eine Funktion, die den String "Hello World" entweder in das File 'filename' schreibt oder wenn 'filename'
None ist einfach in Stdout schreibt.

Denken Sie daran das beides File Streams sind und sie einfach untereinander austauschbar sind (Besitzen beide die
Methode write(). Sie können auch die print() Methode mit dem Argument file benutzen)
"""

import sys


def func(filename=None):
    if filename:
        f = open(filename, "w")
    else:
        f = sys.stdout

    # Makes program independent from stream origin
    f.write("Hello World")

    # Close Stream
    f.close()

    print("Hello World2", file=f)

# Run
func()
func("out.txt")
