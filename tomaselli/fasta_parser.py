import sys
import ws2016 as ws
from argparse import ArgumentParser as Parser
from argparse import FileType
import io




if len(sys.argv) > 1:
	f = open(sys.argv[1], "rb")
	data = ws.parse_fasta(f)
	f.close()

