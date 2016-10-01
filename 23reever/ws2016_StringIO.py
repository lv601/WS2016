#!/usr/bin/python3.5
import io

def parse_fasta3(file_handle):
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

# file_handle = open("long.fasta", 'r')
# parse_fasta3(file_handle)

def get_sequence(data_object, index):
    return data_object[index]["sequence"]

def get_gc_content(data_object, index):
    seq = get_sequence(data_object, index)
    count = seq.count("c") + seq.count("g")
    gc_content = count/len(seq)
    return gc_content