import ws2016 as ws

import sys, io

def parse_console():
    if len(sys.argv) > 1:

        filename = io.open(sys.argv[1], mode="rb")
        file = ws.fasta_parser(filename)

        print(file)
        filename.close()






