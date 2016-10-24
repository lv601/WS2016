#!/usr/bin/python3.5

import ws2016_StringIO
import sys

name = sys.argv[1]
print("filename: ", name)
file_handle = open(name, 'r')
# ws2016_StringIO.parse_fasta3(file_handle)

fasta_list = ws2016_StringIO.parse_fasta3(file_handle)

print(ws2016_StringIO.get_gc_content(fasta_list,0))

print("Done")
