import ws2016 as ws
import sys

if len(sys.argv) >1:
    f=open(sys.argv[1], "rb")
    data=ws.fasta_parser(f)
    f.close()
