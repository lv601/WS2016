# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:57:10 2016

@author: michi
"""

def fasta_file_parser(stream_handle, data_object=None):

    #define function variables
    if data_object is None:
        dataobject =[]    
    data_dict = {}
    lineindex = 0    
    seqreadindex = 0    
    
    stream_handle.read(0)
    #loop over and hang into dictionaries
    for i in stream_handle:
        if i[0] == 62 | ">":
            data_object.append(data_dict)
            
            data_dict["raw"] = i.split(" ")[0]
            data_dict["id"] = i.split(" ")[0][1:]
            data_dict["description"] = i.split(maxsplit=1)[1:]
            #print(i.split(" ")[0][1:])
            
            lineindex = infile_lines.index(i) # = seqidindex
            seqreadindex = lineindex + 1
            data_dict["sequence"] = infile_lines[seqreadindex]
            
        else:
            data_dict["sequence"] += i[:-2]
    return data_object
    
def GC_content(data_object ,index):
    Gcounter=0
    Ccounter=0    
    lenght = len(data_object[index]["sequnce"])
    for letter in data_object[index]["sequnce"]:
        if letter == "G":
            Gcounter += 1
        if letter == "C":
            Ccounter += 1
    percent = (Gcounter+Counter)/length * 100
    return percent

if __name__ == "__main__":
    fasta_file_parser()