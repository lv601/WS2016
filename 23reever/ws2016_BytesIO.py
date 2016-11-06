#!/usr/bin/python3.5
import io

def parse_fasta4(file_handle):
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

#file_handle = open("long.fasta", 'rb')
#print(parse_fasta4(file_handle))

