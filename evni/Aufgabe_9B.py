import time, io

def parse_fasta3(file, db):
    file_handle = open('sequence.fasta','r')

    for line in file_handle:
        datadict = {}
        if line[0] == '>':
           ID, Descr = line[1:].strip().split(maxsplit = 1)
           datadict['ID'] = ID
           datadict['Description'] = Descr
           datadict['raw'] = io.StringIO(line)
           datadict['Sequence'] = io.StringIO()
           db.append(datadict)
           
        else:
            db[-1]['Sequence'].write(line.rstrip())
            db[-1]['raw'].write(line[:-1])
    return(db)
db = []

start1 = time.time()
parse_fasta3('fasta.fa',db)
end1 = time.time()

def parse_fasta4(file, db):
    file_handle = open('sequence.fasta','rb')

    for line in file_handle:
        datadict = {}
        if line[0] == 62:
           ID, Descr = line[1:].strip().split(maxsplit = 1)
           datadict['ID'] = ID
           datadict['Description'] = Descr
           datadict['raw'] = io.BytesIO(line) 
           datadict['Sequence'] = io.BytesIO()
           db.append(datadict)
           
        else:
            db[-1]['Sequence'].write(line.rstrip())
            db[-1]['raw'].write(line[:-1])
    return(db)
db = []

start2 = time.time()
parse_fasta4('fasta.fa',db)
end2 = time.time()
print(("{:.3} seconds".format(end2-start2)) == ("{:.3} seconds".format(end1-start1)))

#Output: True
