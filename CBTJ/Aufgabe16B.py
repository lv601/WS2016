#!/usr/bin/env python3

import io
import ws2016_16B as ws
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('filename', help='Name des Fastafiles')
args = parser.parse_args()
f = open(args.filename, "rb")

data = ws.Parser()
data.pars4fasta_bytearray(f)
f.close()


print (str(data.list_of_dict[0]))

repr_result = repr(data.list_of_dict[0])
print(repr_result)

bytes_result = bytes(data.list_of_dict[0])
print(bytes_result)