import ws2016
import sys

file = open(sys.argv[1],'rb')
parser = ws2016.Parser(file.read())
data = parser.fasta_parser()

try:
    index = int(sys.argv[2])
except:
    index = 0

print('{}: {}'.format(parser.get_id(data,index), parser.get_gc_content(data,index)))