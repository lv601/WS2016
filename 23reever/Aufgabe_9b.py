# Aufgabe 9: fast_paresr3 und fastaparser4 mit StringIO bzw BytesIO

import time
import io

def parse_fasta3(file):
    file_handle = open(file, 'r')
    fastaList = []
    for line in file_handle:
        fastaDict = {}
        #Kopfzeile erkennen
        if line[0] == ">":
            parts = line[1:].strip().split(maxsplit=1)
            # print(parts)
            fastaDict["id"] = parts[0]
            fastaDict["description"] = parts[1]
            fastaDict["raw"] = io.StringIO(line)
            fastaDict["sequence"] = io.StringIO("")
            fastaList.append(fastaDict)
            #print(fastaList)
        else:
            #print(line)
            fastaList[-1]["sequence"].write(line[:-1])
            fastaList[-1]["raw"].write(line)
    return (fastaList)

def parse_fasta4(file):
    file_handle = open(file, 'rb')
    fastaList = []
    for line in file_handle:
        fastaDict = {}
        #Kopfzeile erkennen
        if line[0] == ord(">"):
            parts = line[1:].strip().split(maxsplit=1)
            # print(parts)
            fastaDict["id"] = parts[0]
            fastaDict["description"] = parts[1]
            fastaDict["raw"] = io.BytesIO(line)
            fastaDict["sequence"] = io.BytesIO(b"")
            fastaList.append(fastaDict)
            #print(fastaList)
        else:
            #print(line)
            fastaList[-1]["sequence"].write(line[:-1])
            fastaList[-1]["raw"].write(line)
    return (fastaList)


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

# parse_fasta4("long.fasta")

start = time.time()
parse_fasta3("long.fasta")
end = time.time()
print("Dauer von Fasta Parser 3 mit StringIO in Sekunden: {:.3}".format(end-start))

start = time.time()
parse_fasta4("long.fasta")
end = time.time()
print("Dauer von Fasta Parser 4 mit BytesIO in Sekunden: {:.3}".format(end-start))

start = time.time()
parse_fasta_bytearray("long.fasta")
end = time.time()
print("Dauer von Fasta Parser mit Bytearray in Sekunden: {:.3}".format(end-start))
