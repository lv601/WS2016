var1 = 1
var2 = 2
var3 = 4
var4 = 8
var5 = 16
var6 = 32
var7 = 64
var8 = 128
flags = var1 | var2 | var7 | var8
print(flags)
for i in range(8):
    if flags & 2**i:
        print("Flag ", 2**i , " was set.")