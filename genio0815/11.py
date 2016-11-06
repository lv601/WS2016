#! /usr/bin/python3

import sys
import ws2016 as ws

if len(sys.argv) > 1:  # 0 is prog name

    f = open(sys.argv[1], 'rb')
    reader = ws.parseFastaFile(f)
    f.close()


