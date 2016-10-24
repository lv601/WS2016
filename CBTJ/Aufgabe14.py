#!/usr/bin/env python3

import io
import ws2016_14 as ws
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('filename', help='Name des Fastafiles')
args = parser.parse_args()
f = open(args.filename, "rb")

data = ws.Parser()
data.pars4fasta_bytearray(f)
f.close()

#print (data.get_raw(0))

# ZUM TESTEN
print ("-------ID")
print (data.list_of_dict[0].id)
print ("-------DESCR")
print (data.list_of_dict[0].desc)
print ("-------SEQU")
print (data.list_of_dict[0].seq.getvalue())
print ("-------RAW")
print (data.list_of_dict[0].raw.getvalue())