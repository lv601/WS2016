#!/usr/bin/env python3

import ws2016 as ws
from argparse import ArgumentParser

list_of_dict_bin = []

parser = ArgumentParser()
parser.add_argument('filename', help='Name des Fastafiles')
args = parser.parse_args()

f = open(args.filename, "rb")
data=ws.pars4fasta_bytearray(list_of_dict_bin, f)
f.close()


print ("-------RAW")
print (ws.get_raw (list_of_dict_bin, 0).getvalue())
print ("-------ID")
print (ws.get_id (list_of_dict_bin, 0))
print ("-------DESCR")
print (ws.get_description (list_of_dict_bin, 0))
print ("-------SEQU")
print (ws.get_sequence (list_of_dict_bin, 0).getvalue())