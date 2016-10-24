import sys

def hello(filename=None):
    if filename:
        file = open(filename, 'w')
    else:
        file = sys.stdout

    file.write("Hello World!")
    file.close()

hello()
hello('out.txt')
