#sequence = input("Gib mir einen String: ")
sequence = "0123456789"


def substr(sequence, windowSize):
    output = ""
    for pos in range(0, len(sequence)-windowSize+1):
        output += sequence [pos:pos+windowSize] + " "
    return output

print("Aufgabe 5C:", substr(sequence, 3))

