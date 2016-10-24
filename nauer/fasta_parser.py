#!/usr/bin/env python3

import sys
import ws2016 as ws
from argparse import ArgumentParser as Parser
from argparse import FileType
import io

# Run:
# fasta_parser.py -i seq.fasta -o output
# fasta_parser.py -i seq.fasta
# fasta_parser.py # start terminal line input - type fasta seq and send stream with ctrl+d
# cat seq.fasta | fasta_parser.py -o output
# cat seq.fasta | fasta_parser.py > output

parser= Parser()

# default="-" defines pseudoargument as default -> file stream -> sys.stdin or sys.stdout if mode "w"
# pseudo element allows Unix piping -> cat sequence.fasta | fasta_parser.py works.
# Because of default="-" no extra pseudo element is necessary
parser.add_argument("-i","--input", help="Input filename", type=FileType("rb"), default="-")
parser.add_argument("-o","--output", help="Output filename", type=FileType("w"), default="-")

args = parser.parse_args()

# FileType("rb") or FileType("tb") with the pseudo argument returns the sys.stdin stream object
# sys.stdin has both streams binary and Unicode but sys.stdin directly is Unicode. To get the binary
# stream you have to reference sys.stdin.buffer

# Test if input is sys.stdin and when switch stream to byte stream
if args.input == sys.stdin:
    args.input = args.input.buffer

data = ws.parse_fasta(args.input)

# Because I use streams it does not matter if stream is from file or from standard in/out
print("Id\tGC%", file=args.output)

for index, seq in enumerate(data):
    print("{0}\t{1:.2f}".format(seq['id'].decode(), ws.get_gc_content(data, index)), file=args.output)


# print(ws.__name__, ws.__file__)
# print(__name__)
