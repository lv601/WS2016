sequence = input("Gib mir einen String: ")
windowSize = 3

output = ""
for pos in range(0, len(sequence)-windowSize + 1):
    #direct output
    print(" " * pos, sequence[pos:pos+windowSize], sep="")
    #build up string
    output += sequence [pos:pos+windowSize] + " "

print("Aufgabe 3B:", output)


#Nur zum testen...
def frames(sequence, windowSize=3, frame=1):
    output = ""
    for pos in range(frame, len(sequence)-windowSize+frame, windowSize):
        output += sequence[pos:pos + windowSize] + " "
    return output

#print("Frame (0, Step 3):", frames(sequence,windowSize, 0))
#print("Frame (1, Step 3):", frames(sequence,windowSize, 1))
#print("Frame (2, Step 3):", frames(sequence,windowSize, 2))