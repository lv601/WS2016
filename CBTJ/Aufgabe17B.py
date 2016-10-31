#!/usr/bin/env python3

import io
import ws2016_17B as ws
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('filename', help='Name des Fastafiles')
args = parser.parse_args()
f = open(args.filename, "rb")

data = ws.Parser()
data.pars4fasta_bytearray(f)
f.close()

print(data[1])

for item in data:
    print (item)

print (len(data))