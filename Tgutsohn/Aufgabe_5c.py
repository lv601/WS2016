def sequence(s, ws):
    for i in range(0, len(s)-ws+1):
        print(" " * i, s[i:i+ws], sep="")

sequence("ACGAGTTGCGATGCTA", 3)