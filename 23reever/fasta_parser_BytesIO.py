#!/usr/bin/python3.5

import ws2016_BytesIO
import sys

name = sys.argv[1]
print("filename: ", name)
file_handle = open(name, 'rb')
fasta_list = ws2016_BytesIO.parse_fasta4(file_handle)
print("Done")

