import sys, ws2016 as ws
cmd_name = sys.argv[0]
first_arg = sys.argv[1]

if len(sys.argv) > 1:
	f = open(sys.argv[1], "rb")
	data = ws.parse_fasta(f)
	f.close()

if __name__ == "__main__":
	print(__file__)


