
import sys

def function(filename=None):

    if filename:
        f = open(filename, "w")
    else:
        f = sys.stdout

    f.write("Hello World")
    f.close()

function()
function("hello_world.txt")
