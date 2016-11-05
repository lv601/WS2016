###Aufgabe_11###

import ws2016 as ws
import sys


if len(sys.argv) > 1:
    file = open(sys.argv[1], 'rb')
    data = ws.parse_fasta_bytearray(file)
    print(data)
    file.close()



