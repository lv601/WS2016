import io

eingabe = input("Bitte geben Sie einen beliebigen String ein: ")

#str_io=io.StringIO(print(eingabe))
str_io = open("test", "w+")
str_io.write(eingabe)

print(str_io.tell())
print(len(eingabe))

for i in range(str_io.tell()): #io.TextIOWrapper hat kein len()
    print(str_io.read(3))

#for i in range(len(eingabe) - 3):
#    print(eingabe[i:i+3])
