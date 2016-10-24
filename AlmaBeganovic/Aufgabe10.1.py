#!/usr/bin/env python3
import sys


def func(filename=None):
    if filename:
        f = open(filename, "w")
    else:
        f = sys.stdout

    # Makes program independent from stream origin
    print("Hello World", file=f)

# Run
func()
func("out.txt")