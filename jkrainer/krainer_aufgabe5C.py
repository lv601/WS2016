#Aus einem String immer Blöcke von x rausnehmen


def stringsplitter(sequenz, windowsize):

    a = windowsize
    begin = 0

    for i in range(0, int(len(sequenz)/windowsize)+1):
        print(sequenz[begin:a])
        begin+=windowsize
        a+=windowsize

stringsplitter("ACTCCTTGAAATCGTACGTACA", 3)