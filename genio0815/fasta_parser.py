#! /usr/bin/python3

import sys
import ws2016 as ws

from argparse import ArgumentParser as Parser
from argparse import FileType

parser = Parser(prog='fasta file reader', description="reading fasta files with some output functions implemented ",
                usage='enter an input and output file, file types are automatically detected')

# stick to naming convention used in lecture...
parser.add_argument("-i", "--input", help="Input filename", type=FileType("rb"), default="-")
parser.add_argument("-o", "--output", help="Output filename", type=FileType("w"), default="-")

args = parser.parse_args()

if args.input == sys.stdin:
    args.input = args.input.buffer

read = ws.parseFastaFile(args.input)

for index, seq in enumerate(read):
    print("{0}\t{1:.2f}".format(seq['id'].decode(), ws.getBaseContentAbs(read, 0, "g"), file=args.output))

#if len(sys.argv) > 1:  # 0 is prog name
#
#    with open(sys.argv[1], 'rb') as f:
#        reader = ws.parseFastaFile(f)
#
#    print(ws.getGCcontent(reader, 0))
#    print("raw content of base {0:} in file {1:} is {2:}"
#          .format("g", sys.argv[1], ws.getBaseContentAbs(reader, 0, "G")))