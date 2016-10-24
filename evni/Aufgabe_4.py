var1=1
var2=2
var3=4
var4=8
var5=16
var6=32
var7=64
var8=128
var9=256

flags = var1 | var3 | var9

print(flags)
for i in range(9):
    if flags & 2**i:
        print('flag', 2**i, 'was set ')

