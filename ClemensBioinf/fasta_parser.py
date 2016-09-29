import ws2016
import sys

file = open(sys.argv[1],'r')
data = ws2016.fasta_parser(file.read())

try:
    index = int(sys.argv[2])
except:
    index = 0

# Enter attribute function you want to use (see ws2016.py)
print('{}: {}'.format(ws2016.get_id(data,index), ws2016.get_gc_content(data,index)))
