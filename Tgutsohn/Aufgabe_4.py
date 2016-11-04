F0 = 1
F1 = 2
F2 = 4
F3 = 8
F4 = 16
F5 = 32
F6 = 64
F7 = 128
F8 = 256

flags = F2 | F5 | F6| F8

for i in range(9):
    if flags & 2**i:
        print("The Flag", 2**i, "was set.")