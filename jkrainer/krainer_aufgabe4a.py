VAR1 = 1
VAR2 = 2
VAR3 = 4
VAR4 = 8
VAR8 = 128

flags = VAR1 | VAR3 | VAR8 | VAR4

print(flags)

for i in range(8):
    if flags & 2**i:
        print("Flag ", 2**i, " was set.")