def parse_fasta(file):
    file_handle = open(file, "r")
    db = None
    for line in file_handle:
        if line[0] == 62:
            if db:
                yield db
            ident, desc = line[1:].strip().split(maxsplit=1)
            db = {'id': ident, 'description': desc, 'sequence': ""}
        else:
            db['sequence'] += line.rstrip()
    else:
        yield db