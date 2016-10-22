#!/usr/bin/env python3

import sys
import ws2016 as ws

list_of_dict_bin = []

if len(sys.argv)>1:
    f= open(sys.argv[1], "rb")
    data=ws.pars4fasta_bytearray(list_of_dict_bin, f)

    f.close()

#print(list_of_dict_bin)

print ("-------RAW")
print (ws.get_raw (list_of_dict_bin, 0).getvalue())
print ("-------ID")
print (ws.get_id (list_of_dict_bin, 0))
print ("-------DESCR")
print (ws.get_description (list_of_dict_bin, 0))
print ("-------SEQU")
print (ws.get_sequence (list_of_dict_bin, 0).getvalue())