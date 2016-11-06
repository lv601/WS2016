def parse_fasta(file):
    file_handle = open('sequence.fasta', 'r')
    db = None

    for line in file_handle:
        if line[0] == '>':
            if db:
                yield db
            ID, Desc = line[1:].strip().split(maxsplit=1)
            db = {'ID': ID, 'Description': Desc, 'Sequence': ''}
        else:
            db['Sequence'] += line.rstrip()
    else:
        yield db
#for result in parse_fasta('sequence.fasta'):
 #   print(result['ID'], result['Description'], len(result['Sequence']))
                
Seq = parse_fasta('sequence.fasta')
pprint(next(Seq))



