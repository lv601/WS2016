
import sys
cmd_name = sys.argv[0]
first_arg = sys.argv[1]


import ws2016 as ws
if len(sys.argv) > 1:
	f = open(sys.argv[1], "rb")
	data = ws.parse_fasta(f)
	f.close()

if __name__ == "__main__":
# Run test code
	print(__file__)


