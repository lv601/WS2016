# Aufgabe 8: Verwendung von bytearrays statt strings (basierend auf Aufgabe 6a)

import time

def parse_fasta_bytearray(file):
    file_handle = open(file, "rb")
    fastaList = []
    for line in file_handle:
        fastaDict = {}
        #Kopfzeile erkennen
        if line[0] == ord(">"):
            parts = line[1:].strip().split(maxsplit=1)
            #print(parts)
            fastaDict["id"] = parts[0]
            fastaDict["description"] = parts[1]
            fastaDict["raw"] = line
            fastaDict["sequence"] = bytearray()
            fastaList.append(fastaDict)
            #print(fastaList)
        else:
            #print(type(line))
            fastaList[-1]["sequence"] += bytearray(line[:-1])
            fastaList[-1]["raw"] += line
    return(fastaList)

# Ueberarbeitete Aufgabe 6a:

def parse_fasta(file):
    file_handle = open(file, 'r')
    fastaList = []
    for line in file_handle:
        fastaDict = {}
        #Kopfzeile erkennen
        if line[0] == ">":
            parts = line[1:].partition(" ")
            fastaDict["id"] = parts[0]
            fastaDict["description"] = parts[2]
            fastaDict["raw"] = line
            fastaDict["sequence"] = ""
            fastaList.append(fastaDict)
        else:
            fastaList[-1]["sequence"] += line[:-1]
            fastaList[-1]["raw"] += line
    return(fastaList)


start = time.time()
parse_fasta("long.fasta")
end = time.time()
print("Dauer von Fasta Parser mit Str in Sekunden: {:.3}".format(end-start))
start = time.time()
parse_fasta_bytearray("long.fasta")
end = time.time()
print("Dauer von Fasta Parser mit Bytearray in Sekunden: {:.3}".format(end-start))
