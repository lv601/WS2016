VAR1 = 1
VAR2 = 2
VAR3 = 4
VAR4 = 8
VAR5 = 16
VAR6 = 32
VAR7 = 64
VAR8 = 128
VAR9 = 256

flags = VAR1 | VAR6 | VAR7

for i in range(9):
    if flags & 2**i:
        print("Flag ", 2**i, " was set.")


for i in range(9):
    if flags & 1<<i:
        var = i+1
        print("Var",var,"was set" )