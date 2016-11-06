import io
import time
import re
from pprint import pprint

def parse_fasta(db, file_name):
    
    file_handle = open(file_name, "r")

    for line in file_handle:
        if line[0] == ">": ### zahl da > nicht gelesen werden kann da bytes
            # New fasta sequence starts - parse header
            ident, desc = line[1:].strip().split(maxsplit=1)

            # Create new sequence entry in db
            db.append({'id': ident, 'description': desc,'sequence': "", 'raw': line})
        else:
            # Sequence line
            db[-1]['sequence'] += (line.rstrip())
            db[-1]['raw'] += (line)




def parse_fasta1(db, file_name):
   
    file_handle = open(file_name, "br")

    for line in file_handle:
        if line[0] == 62: ### zahl da > nicht gelesen werden kann da bytes
            # New fasta sequence starts - parse header
            ident, desc = line[1:].strip().split(maxsplit=1)

            # Create new sequence entry in db
            db.append({'id': ident, 'description': desc,'sequence': bytearray(), 'raw': bytearray(line)})
        else:
            # Sequence line
            db[-1]['sequence'] += (line.rstrip())
            db[-1]['raw'] += (line)


def parse_fasta2(db, file_name):
   
    file_handle = open(file_name, "br")

    for line in file_handle:
        if line[0] == 62: ### zahl da > nicht gelesen werden kann da bytes
            # New fasta sequence starts - parse header
            ident, desc = line[1:].strip().split(maxsplit=1)

            # Create new sequence entry in db
            db.append({'id': ident, 'description': desc,'sequence': io.BytesIO(), 'raw': io.BytesIO(line)})
        else:
            # Sequence line
            db[-1]['sequence'].write(line.rstrip())
            db[-1]['sequence'].write(line)
	#print bytes_io.getvalue()
	#return bytes_io


def parse_fasta3(db, file_name):
    
    f = open(file_name, "r")
    for line in f:
        if line[0] == ">":
            # New fasta sequence starts - parse header
            ident, desc = line[1:].strip().split(maxsplit=1)

            # Create new sequence entry in db
            db.append({'id': ident, 'description': desc, 'sequence': io.StringIO(), 'raw': io.StringIO(line)})
        else:
            # Sequence line
            db[-1]['sequence'].write(line.rstrip())
            db[-1]['sequence'].write(line)	
	#print(str_io.getvalue())
	#return str_io
	

data = []
start = time.time()
parse_fasta1(data, "sequence.fasta")
end = time.time()
print("{:.3} seconds".format(end-start))
print(data)

data = []
start = time.time()
parse_fasta2(data, "sequence.fasta")
end = time.time()
print("{:.3} seconds".format(end-start))
print(data)

data = []
start = time.time()
parse_fasta3(data, "sequence.fasta")
end = time.time()
print("{:.3} seconds".format(end-start))
print(data)

data = []
start = time.time()
parse_fasta(data, "sequence.fasta")
end = time.time()
print("{:.3} seconds".format(end-start))
print(data)