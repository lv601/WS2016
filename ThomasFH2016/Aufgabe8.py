def parse_fasta_str(file, db):
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

def parse_fasta_byte(file, db):
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

def mytimer(func, *args, **kargs):
    import time
    start = time.time()
    result = func(*args, **kargs)
    end = time.time()
    return "{:.3}".format(end-start)

d=[]

print("Start")

print("String_Parsing:", mytimer(parse_fasta_str, "../examples/long.fasta", db=d))
print("Bytearray_Parsing:", mytimer(parse_fasta_byte, "../examples/long.fasta", db=d))

print("Ende")
