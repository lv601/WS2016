def sequence(sequenz, ws):
    for i in range(0, len(sequenz)-ws+1):
        print(" " * i, sequenz[i:i+ws], sep="")

sequence("ATTAGGAGTTGCGATGCTA", 3)