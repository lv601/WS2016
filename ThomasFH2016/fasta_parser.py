#!/usr/bin/env python

import sys
import ws2016 as ws

#sys.argv[0] - prorgam name
#sys.argv[1] - first argument
if len(sys.argv) > 1:
    data = []
    with open(sys.argv[1], "rb") as f:
        data.append(ws.parse_fasta(f))
        data.append(ws.parse_fasta(f))

print(len(data))