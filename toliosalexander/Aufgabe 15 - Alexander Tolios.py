### Aufgabe 15 - Alexander Tolios - last modified 29.10.2016 

def parse_fasta(file_name):
    file_handle = open(file_name, "r")
    db = 0 # None
    for line in file_handle:
        if line[0] == ">":
            if db:  # return if db has an full entry
                yield db
            ident, desc = line[1:].strip().split(maxsplit=1)
            db = {'id': ident, 'desc': desc, 'seq': ""}
        else:
            db['seq'] += line.rstrip()
    else:
        yield db  # return last entry

'''
for seq in parse_fasta("../examples/sequence.fasta"):
    print(seq['id'], seq['desc'], "\nSeq. Length: {}".format(len(seq['seq'])))
'''
################## CAVE: funktioniert noch nicht!

for seq in parse_fasta("../examples/sequence.fasta"):
    next(seq['id'], seq['desc'], "\nSeq. Length: {}".format(len(seq['seq'])))


