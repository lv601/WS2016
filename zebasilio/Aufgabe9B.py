# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:29:15 2016

@author: jose
"""

import time, io


#string +=
def fasta_parser_1 (path, data):
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
    return(data)
data = []
#pprint(data)
   # print (len(data))
#fasta_parser_1('/home/jose/Downloads/Introduction to Programing/long.fasta', data)



start1=time.time()
fasta_parser_1('/home/jose/Downloads/Introduction to Programing/long.fasta', data)
end1=time.time()
print ("{:.3} seconds".format(end1 - start1))

#byterray
def fasta_parser_2(path, data):
    file_handle = open(path, 'rb')
    data = []
    for line in file_handle:
        dic = {}
        if line[0] == 62:
            id, description = line [1:].strip().split(maxsplit=1)
            dic['ID'] = id
            dic['Description'] = description
            dic['Sequence'] = bytearray()
            dic ['raw'] = bytearray(line)
            data.append(dic)
        else:
            data [-1]['Sequence'] += line.rstrip()
            data [-1]['raw'] +=line
    return(data)
data = []

start2=time.time()
fasta_parser_2('/home/jose/Downloads/Introduction to Programing/long.fasta', data)
end2=time.time()
print ("{:.3} seconds".format(end2 - start2))

#bytesIO
def fasta_parser_3(path, data):
    file_handle = open(path, 'rb')
    data = []
    for line in file_handle:
        dic = {}
        if line[0] == 62:
            id, description = line [1:].strip().split(maxsplit=1)
            dic['ID'] = id
            dic['Description'] = description
            dic['Sequence'] = io.BytesIO()
            dic ['raw'] = io.BytesIO(line)
            data.append(dic)
        else:
            data [-1]['Sequence'].write(line.rstrip())
            data [-1]['raw'].write(line)
    return(data)
data = []

start3=time.time()
fasta_parser_3('/home/jose/Downloads/Introduction to Programing/long.fasta', data)
end3=time.time()
print ("{:.3} seconds".format(end3 - start3))



#StringIO
def fasta_parser_4(path, data):
    file_handle = open(path, 'r')
    data = []
    for line in file_handle:
        dic = {}
        if line[0] == ">":
            id, description = line [1:].strip().split(maxsplit=1)
            dic['ID'] = id
            dic['Description'] = description
            dic['Sequence'] = io.StringIO()
            dic ['raw'] = io.StringIO(line)
            data.append(dic)
        else:
            data [-1]['Sequence'].write(line.rstrip())
            data [-1]['raw'].write(line)
    return(data)
data = []
#pprint(data)
   # print (len(data))
#fasta_parser_1('/home/jose/Downloads/Introduction to Programing/long.fasta', data)
start4=time.time()
fasta_parser_4('/home/jose/Downloads/Introduction to Programing/long.fasta', data)
end4=time.time()
print ("{:.3} seconds".format(end4 - start4))

print ("{:.3} seconds".format(end2 - start2) == ("{:.3} seconds".format(end1 - start1)))
print ("{:.3} seconds".format(end4 - start4) == ("{:.3} seconds".format(end3 - start3)))