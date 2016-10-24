import time
from pprint import pprint

def parse_fasta(file, db):
    file_handle = open('sequence.fasta','r')

    for line in file_handle:
        datadict = {}
        if line[0] == '>':
           ID, Descr = line[1:].strip().split(maxsplit = 1)
           datadict['ID'] = ID
           datadict['Description'] = Descr
           datadict['raw'] = line 
           datadict['Sequence'] = ''
           db.append(datadict)
           
        else:
            db[-1]['Sequence'] += (line.rstrip())
            db[-1]['raw'] += (line[:-1])
    return(db)
db = []
#pprint(parse_fasta('sequence.fasta', db))


start1 = time.time()
parse_fasta('fasta.fa',db)
end1 = time.time()
#print("{:.3} seconds".format(end1-start1))



def parse_fasta_bytearray(file, db):
    file_handle = open('sequence.fasta','rb')

    for line in file_handle:
        datadict = {}
        if line[0] == 62:
           ID, Descr = line[1:].strip().split(maxsplit = 1)
           datadict['ID'] = ID
           datadict['Description'] = Descr
           datadict['raw'] = bytearray(line) 
           datadict['Sequence'] = bytearray()
           db.append(datadict)
           
        else:
            db[-1]['Sequence'] += (line.rstrip())
            db[-1]['raw'] += (line[:-1])
    return(db)
db = []
#pprint(parse_fasta_bytearray('sequence.fasta', db))


start2 = time.time()
parse_fasta_bytearray('fasta.fa',db)
end2 = time.time()
print(("{:.3} seconds".format(end2-start2)) == ("{:.3} seconds".format(end1-start1)))
