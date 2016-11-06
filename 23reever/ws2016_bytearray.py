#!/usr/bin/python3.5
import io

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