import re
re.IGNORECASE

V1 = 1
V2 = 2
V3 = 4
V4 = 8
V5 = 16
V6 = 32
V7 = 64
V8 = 128

pruef = V1 | V2 | V6 | V8

for i in range(8):
    if pruef & 2**i:
        print("{} set.".format(2**i))
