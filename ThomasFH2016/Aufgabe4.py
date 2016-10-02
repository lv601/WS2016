# TIPP: Verwenden Sie für Konstanten wie diese uppercase Notation FLAG1, FLAG2, ...
# Sehen sie z.B. das Modul re
# import re
# re.IGNORECASE
Flag1 = 2
Flag2 = 4
Flag3 = 8
Flag4 = 16
Flag5 = 32
Flag6 = 64
Flag7 = 128
Flag8 = 256


def foo(flag):
    if flag & Flag1:
        print("Flag1")
    if flag & Flag2:
        print("Flag2")
    if flag & Flag3:
        print("Flag3")
    if flag & Flag4:
        print("Flag4")
    if flag & Flag5:
        print("Flag5")
    if flag & Flag6:
        print("Flag6")
    if flag & Flag7:
        print("Flag7")
    if flag & Flag8:
        print("Flag8")

    for i in range(8):
        t = 1 << i

        if flag & 2**i:
            print("Flag ", 2**i, " was set")

foo(Flag7 | Flag2)
