def write2file(filename=None, Text=""):
    if filename:
        file = open(filename, "w+")
        file.write(Text)
        file.seek(0)
        print("In file ", filename,":",file.read())
        file.close()
    else:
        print("No filename given. Sdtout:",Text)

write2file(filename="Hello", Text="Hello World")
write2file(Text="Hello World")

# TIPP: Sie können die Streamobjekte einfach austauschen. Somit brauchen Sie keine doppelte redundante Logik aufbauen
import sys

def write2file(filename=None, text=""):
    if filename:
        f = open(filename, "w+")
    else:
        f = sys.stdout

    f.write(text + "\n")
    # or alternative
    print(text, file=f)
    f.close()

write2file(text="Hello World")