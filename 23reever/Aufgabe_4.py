# Aufgabe 4
# Uppercase - weil konstante
# Vergleich el. Schalter

VAR0 = 1
VAR1 = 2
VAR2 = 4
VAR3 = 8
VAR4 = 16
VAR5 = 32
VAR6 = 64
VAR7 = 128
VAR8 = 256

flags = VAR0 | VAR2 | VAR8

# print(flags)

for i in range(9):
    if flags & 2**i:
        print("Flag ", 2**i, " was set.")

# for i in range(8):
#     if flags & VAR2:
#         print("Flag ", 2**i, " was set.")


# vgl flag und binärwert - VAR2 = 4, vgl mit binärer 4 (0b100) -> wenn okay output 4
# print(flags & 0b100)
# wenn nicht ok -> output 0
# print(flags & 0b100000)

# x = 1
# print(x)

# for x in range(10):
#     y = x
#
# print(x)
# print(y)