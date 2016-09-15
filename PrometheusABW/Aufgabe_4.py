# TIPP: Verwenden Sie für Konstanten wie diese uppercase Notation N1, N2, ...
# Sehen sie z.B. das Modul re
# import re
# re.IGNORECASE
flaglist = []
a=2
b=4
c=8
d=16
e=32
f=64
g=128
h=256

flags = a | b 

print(flags)
print(bin(flags))

for i in range(8):
	if flags & 2**i:
		flaglist.append(2**i)
		
print("The flags are set:", flaglist)



