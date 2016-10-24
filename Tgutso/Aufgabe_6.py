from pprint import pprint

file_handle = open("/home/gutsohn/WS2016/examples/sequence.fasta", "r")

db = []
for line in file_handle:

    if line[0] == ">":
        id, description = line.split(maxsplit=1)
        db.append({'raw' : line, 'id': id.lstrip(">"), 'description': description, 'sequence': ""})
    else:
        db[-1]['sequence'] += line.rstrip()
        db[-1]['raw'] += line
