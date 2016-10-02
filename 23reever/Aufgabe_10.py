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

