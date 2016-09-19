import time, io


def parse_fasta_string(file, db):
    file_handle = open(file, 'r')
    for line in file_handle:
        if line[0] == '>':
            ident, desc = line[1:].strip().split(maxsplit=1)
            db.append({'id': ident,
                             'description': desc,
                             'sequence': "",
                              'raw': line})
        else:
            db[-1]['sequence'] += line.rstrip()
            db[-1]['raw'] += line


def parse_fasta_bytearray(file, db):
    file_handle = open(file, 'rb')
    for line in file_handle:
        if line[0] == ord('>'):
            ident, desc = line[1:].strip().split(maxsplit=1)
            db.append({'id': ident,
                             'description': desc,
                             'sequence': bytearray(),
                              'raw': bytearray(line)})
        else:
            db[-1]['sequence'] += (line.rstrip())
            db[-1]['raw'] += (line)


def parse_fasta_stringio(file, db):
    file_handle = open(file, 'r')
    for line in file_handle:
        if line[0] == '>':
            ident, desc = line[1:].strip().split(maxsplit=1)
            db.append({'id': ident,
                             'description': desc,
                             'sequence': io.StringIO(),
                              'raw': io.StringIO(line)})
        else:
            db[-1]['sequence'].write(line.rstrip())
            db[-1]['raw'].write(line)


def parse_fasta_bytesio(file, db):
    file_handle = open(file, 'rb')
    for line in file_handle:
        if line[0] == ord('>'):
            ident, desc = line[1:].strip().split(maxsplit=1)
            db.append({'id': ident,
                             'description': desc,
                             'sequence': io.BytesIO(),
                              'raw': io.BytesIO(line)})
        else:
            db[-1]['sequence'].write(line.rstrip())
            db[-1]['raw'].write(line)




def mytimer(func, *args, **kargs):
    start = time.time()
    result = func(*args, **kargs)
    end = time.time()
    return "{:.3}".format(end-start)

d = []

print("Start")
print("Datatype(String):", mytimer(parse_fasta_string,"../examples/long.fasta", db=d))
print("Datatype(Bytesarray):", mytimer(parse_fasta_bytearray, "../examples/long.fasta", db=d))
print("Datatype(StringIO):", mytimer(parse_fasta_stringio,"../examples/long.fasta", db=d))
print("Datatype(BytesIO):", mytimer(parse_fasta_bytesio,"../examples/long.fasta", db=d))
print("Ende")