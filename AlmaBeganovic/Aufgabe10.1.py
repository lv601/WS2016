import sys


def func(filename=None):
    if filename:
        f = open(filename, "w")
    else:
        f = sys.stdout

    print("Hello World", file=f)

func()
func("out.txt")