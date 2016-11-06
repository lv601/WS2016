def parse_fasta(infile):

    db = None
    with open(infile,'r') as f:
        for line in f:
            if line[0] == ">":
                if db:
                    yield db
                    db = None

                ident, desc = line[1:].strip().split(maxsplit=1)

                db = {'id': ident, 'desc': desc, 'seq': "", 'raw': line}
            else:
                db['seq'] += line.rstrip()
                db['raw'] += line
        else:  # catch last element
            yield db

# test
for seq in parse_fasta("../examples/long.fasta"):
    print(seq['id'], seq['desc'], "\nSeq. Length: {}".format(len(seq['seq'])))