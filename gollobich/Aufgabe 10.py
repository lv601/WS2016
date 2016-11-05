from sys import stdout

def write_hello_word(filename=None):
    if filename:
        file = open(filename,'w')
    else:
        file = stdout

    file.write("Hello World!")
    file.close()

write_hello_word()
write_hello_word('test.txt')
