#!/usr/bin/env python3

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
func("out.txt")
