#!/usr/bin/env python3

import sys
import ws2016 as ws

if len(sys.argv) > 1:
    with open(sys.argv[1], "rb") as f:
        data = ws.parse_fasta(f)

        print("Id\tGC%")

        for index, seq in enumerate(data):
            print("{0}\t{1:.2f}".format(seq['id'].decode(), ws.get_gc_content(data, index)))
else:
    print("Run fasta_parser.py <filename>", file=sys.stderr)