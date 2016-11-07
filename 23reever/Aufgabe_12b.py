#!/usr/bin/python3.5

import ws2016_bytearray
import sys
import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('input', help='name of input file', type=argparse.FileType("rb"))
args = parser.parse_args()
fasta_list = ws2016_bytearray.parse_fasta_bytearray(args.input)
#print(fasta_list)
print("DONE")
