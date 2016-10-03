import sys

def helloworld(filename=None):
    if filename:
        f=open(filename, "w")
    else:
        f=sys.stdout
    f.write("Hello World")
helloworld()
helloworld("out.txt")
