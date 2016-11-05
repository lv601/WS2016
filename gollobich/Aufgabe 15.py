# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:44:05 2016

@author: lv
"""

def fasta_parser(filename):
    """fasta parser, reads fasta file and introduces content into list"""
    file_handle = open(filename, "r")
    for index, line in enumerate(file_handle):
        if line[0] == ">":
            header, desc = line.split(maxsplit=1)
            header = header[1:]
            desc = desc.strip()
            if index == 0:
                db = [{"id": header, "desc": desc, "sequence": ""}]
            else:
                db.append({"id":header, "desc":desc, "sequence": ""})
        else:
            line = line.strip()
            db[-1]['sequence']+= (line)
            yield db
    else:
        yield db

parsing = fasta_parser("../examples/sequence.fasta")

for i in parsing: #ueber den Generator kann iteriert werden
    print(i)
