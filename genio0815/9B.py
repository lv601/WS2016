import time
import io

def parseFastaFile1(infile, db):
    with open(infile, 'r') as inFile:
        for line in inFile:
            if line[0] == ">":
                ident, desc = line[1:].strip().split(maxsplit=1)
                db.append({'id': ident, 'description': desc, 'sequence': "", 'raw': line})
            else:
                db[-1]['sequence'] += line.rstrip()
                db[-1]['raw'] += line


def parseFastaFile2(infile, db):
    with open(infile, "rb") as inFile:
        for line in inFile:
            if line[0] == 62:  # bin token for ">"
                ident, desc = line[1:].strip().split(maxsplit=1)
                db.append({'id': ident,
                           'description': desc,
                           'sequence': bytearray(),
                           'raw': bytearray(line)})
            else:
                db[-1]['sequence'] += (line.rstrip())
                db[-1]['raw'] += (line)

# version using StringIO
def parseFastaFile3(infile, db):
    with open(infile, "r") as inFile:
        for line in inFile:
            if line[0] == ">":
                ident, desc = line[1:].strip().split(maxsplit=1)
                db.append({'id': ident,
                           'description': desc,
                           'sequence': io.StringIO(),
                           'raw': io.StringIO(line)})
            else:
                db[-1]['sequence'].write(line.rstrip())
                db[-1]['raw'].write(line)


# version using BytesIO
def parseFastaFile4(infile, db):
    with open(infile, "rb") as inFile:
        for line in inFile:
            if line[0] == 62:  # bin token for ">"
                ident, desc = line[1:].strip().split(maxsplit=1)
                db.append({'id': ident,
                           'description': desc,
                           'sequence': io.BytesIO(),
                           'raw': io.BytesIO(line)})
            else:
                db[-1]['sequence'].write(line.rstrip())
                db[-1]['raw'].write(line)

# Stop time of function calls
def stop_time(func, *args, **kargs):
    start = time.time()

    result = func(*args, **kargs)

    end = time.time()
    print("Function {} takes {:.3} seconds".format(func.__name__, end - start))
    return result

d = []

res1 = stop_time(parseFastaFile1, "../examples/long.fasta", db=d)
res2 = stop_time(parseFastaFile2, "../examples/long.fasta", db=d)
res3 = stop_time(parseFastaFile3, "../examples/long.fasta", db=d)
res4 = stop_time(parseFastaFile4, "../examples/long.fasta", db=d)

# Compare both sequences
print(d[0]['sequence'] == d[1]['sequence'].decode())
print(d[0]['sequence'] == d[2]['sequence'].getvalue())
print(d[0]['sequence'] == d[3]['sequence'].getvalue().decode())