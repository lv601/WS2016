# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:52:55 2016

@author: jose
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:31:33 2016

@author: jose
"""

import time

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



start1=time.time()
fasta_parser_1('/home/jose/Downloads/Introduction to Programing/long.fasta', data)
end1=time.time()
print ("{:.3} seconds".format(end1 - start1))


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

print (("{:.3} seconds".format(end2 - start2)) == ("{:.3} seconds".format(end1 - start1)))


#def time_counter(func, *args, **kargs):
 #   start = time.time()
    
  #  result = func(*args, **kargs)
    
   # end = time.time()
    
    #print ("Function {} takes {:.3} seconds".format(func.__name__, end - start))
    #return result

#d = []


#t1 = time_counter(fasta_parser_1 ,'/home/jose/Downloads/Introduction to Programing/long.fasta', data=d)
#t2 = time_counter(fasta_parser_2 ,'/home/jose/Downloads/Introduction to Programing/long.fasta', data=d)

#print(d[0]['Sequence'] == d[1]['Sequence'])