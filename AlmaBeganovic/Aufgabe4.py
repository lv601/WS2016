# TIPP: Verwenden Sie für Konstanten wie diese uppercase Notation N1, N2, ...
# Sehen sie z.B. das Modul re
# import re
# re.IGNORECASE
n1 = 2
n2 = 4
n3 = 8
n4 = 16
n5 = 32
n6 = 64
n7 = 128
n8 = 256
flags = n1 | n3 | n8
print (flags)

def func (flag):
    for i in range(8):
        if flags & 2**1:
            print("Flags", 2**i, "was set.")
