#!/usr/bin/env python3
import sys


def func(filename=None):
    if filename:
        f = open(filename, "w")
    else:
        f = sys.stdout

    f.write("Hello World")

func()
func("out.txt")