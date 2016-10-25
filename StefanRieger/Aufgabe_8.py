import time

def fasta_parser1(file, db):
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

def fasta_parser2(file, db):
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

def timer(func, *args, **kargs):

    start = time.time()
    result = func(*args, **kargs)
    end = time.time()
    print('Function {} takes {:.3} seconds'.format(func.__name__, end - start))

d=[]

t1 = time(fasta_parser2(), "../examples/long.fasta", db=d)
t2 = time(fasta_parser1(), "../examples/long.fasta", db=d)

# Compare both sequences
print(d[0]['sequence'] == d[1]['sequence'].decode())