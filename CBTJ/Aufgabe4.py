
BitVar = [1,2,4,8,16,32,64,128]

BitCalc= BitVar[0]|BitVar[4]|BitVar[6]

print(BitCalc)

for i in BitVar:
    if BitCalc & i:
        print ("Flagposition", BitVar.index(i), "is True")
        print ("Flag", i, "was set")

