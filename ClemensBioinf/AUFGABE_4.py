v1 = 1
v2 = 2
v3 = 4
v4 = 8
v5 = 16
v6 = 32
v7 = 64
v8 = 128

pruef = v1 | v2 | v6 | v8

print(pruef)

for i in range(8):
    if pruef & 2**i:
        print("{} set.".format(2**i))

