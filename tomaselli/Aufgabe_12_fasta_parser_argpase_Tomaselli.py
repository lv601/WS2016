import argparse
import ws2016 as ws



parser = argparse.ArgumentParser(prog='PROG')

parser.add_argument('-input', help='name of input file', type=argparse.FileType("r", encoding='UTF-8'))
parser.add_argument('-o','--output' , help='name of output file', type=argparse.FileType("w", encoding='UTF-8'), default="-")

args = parser.parse_args()
data = ws.parse_fasta(args.input)
args.output.write(str(data))
