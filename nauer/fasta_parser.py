#!/usr/bin/env python3

import sys
import ws2016 as ws
from argparse import ArgumentParser as Parser
from argparse import FileType
import io

parser= Parser()

parser.add_argument("filename", help="Filename", type=FileType("rb"))

args = parser.parse_args()

data = ws.parse_fasta(args.filename)

print("Id\tGC%")

for index, seq in enumerate(data):
    print("{0}\t{1:.2f}".format(seq['id'].decode(), ws.get_gc_content(data, index)))


# print(ws.__name__, ws.__file__)
# print(__name__)
