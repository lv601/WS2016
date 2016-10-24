import time, io


def fasta_parser3(file, db):
    file_handle = open('sequence.fasta', 'r')

    for line in file_handle:
        dd = {}
        if line[0] == '>':
            id, des = line[1:].strip().split(maxsplit=1)
            dd['ID'] = id
            dd['Description'] = des
            dd['raw'] = io.StringIO(line)
            dd['Sequence'] = io.StringIO()
            db.append(dd)

        else:
            db[-1]['Sequence'].write(line.rstrip())
            db[-1]['raw'].write(line[:-1])
    return (db)


def fasta_parser4(file, db):
    file_handle = open('sequence.fasta', 'rb')

    for line in file_handle:
        dd = {}
        if line[0] == 62:
            id, des = line[1:].strip().split(maxsplit=1)
            dd['ID'] = id
            dd['Description'] = des
            dd['raw'] = io.BytesIO(line)
            dd['Sequence'] = io.BytesIO()
            db.append(dd)

        else:
            db[-1]['Sequence'].write(line.rstrip())
            db[-1]['raw'].write(line[:-1])
    return (db)


db = []

start = time.time()
fasta_parser3("../examples/long.fasta")
end = time.time()
print("StringIO Parser braucht {:.3} Sekunden".format(end-start))

start = time.time()
fasta_parser4("../examples/long.fasta")
end = time.time()
print("BytesIO Parser braucht {:.3} Sekunden".format(end-start))