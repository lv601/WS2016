#Aufgabe 15
import re
from pprint import pprint
#db = database, dict for info
def parse_fasta(db, file_name):
    infile=open(file_name,"r")

    for line in infile:
        if line[0]==">":
            if db: #return if db has a full entry
                yield db

            ident, desc=line[1:].strip().split(maxsplit=1)
            db.append({"id":ident, "description":desc,"sequence":"","raw":line})
        else:
            db[-1]["sequence"]+= line.rstrip()
            db[-1]["raw"]+=line
    else:
        yield db #return last entry
                
for seq in parse_fasta("../examples/sequence.fasta"): #theres a problem here
    print(seq['id'], seq['desc'], "\nSeq. Length: {}".format(len(seq['seq'])))