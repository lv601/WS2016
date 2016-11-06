# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:31:33 2016

@author: jose
"""

from pprint import pprint

def fasta_parser (path):
    file_handle = open(path, 'r')
    data = []
    for line in file_handle:
        dic = {}
        if line[0] == ">":
            id, description = line [1:].strip().split(maxsplit=1)
            dic['ID'] = id
            dic['Description'] = description
            dic['Sequence'] = ""
            dic ['raw'] = line
            data.append(dic)
        else:
            data [-1]['Sequence'] += line.rstrip()
            data [-1]['raw'] +=line
            
    pprint(data)
    print (len(data))
fasta_parser('/home/jose/Downloads/Introduction to Programing/sequence.fasta')
            
    