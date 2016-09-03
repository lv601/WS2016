# 8 Variablen mit einer Bit Position von 1 bis 256
var1 = 1
var2 = 2
var3 = 4
var4 = 8
var5 = 16
var6 = 64
var7 = 128
var8 = 256

flags = var1 | var3 | var8

print(flags)

for i in range(8):
    if flags & 2**i:
        print("Flag ", 2**i, " was set.")