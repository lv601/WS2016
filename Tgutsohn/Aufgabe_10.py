import sys

def function(filename=None):
    if filename:
        f = open(filename, "w")
        f.write(("Hello World"))
    else:
        f = sys.stdout
        f.write("Hello World")
        f.close()

function()
function("out.txt")