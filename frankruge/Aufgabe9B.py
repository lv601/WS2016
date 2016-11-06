import io
import time

def parse_fasta(file, db):
    file_handle = open(file, "r")


    for line in file_handle:
        if line.startswith(">"):
            description, id = line[1:].split(maxsplit=1) #zweigeteilt
            db.append({'id': id,
                       'description': description,
                       'sequence': "",
                       'raw': line})
        else:
            db[-1]['sequence'] += line.rstrip() # [-1] because for loop is one ahead
            db[-1]['raw'] += line


def parse_fasta_binary(file, db):
    file_handle = open(file, "rb")

    for line in file_handle:
        if line[0] == 62:
            description, id = line[1:].split(maxsplit=1) 
            db.append({'id': id,
                       'description': description,
                       'sequence': bytearray(),
                       'raw': bytearray()})
        else:
            db[-1]['sequence'] += line.rstrip()
            db[-1]['raw'] += line
        #pprint(db)


def parse_fasta_IO(file, db):
    file_handle = open(file, "r")


    for line in file_handle:
        if line.startswith(">"):
            description, id = line[1:].split(maxsplit=1) #zweigeteilt
            db.append({'id': id,
                       'description': description,
                       'sequence': io.StringIO(),
#			io.StringIO(line)})
                       'raw': io.StringIO(line)})
        else:
            db[-1]['sequence'].write(line.rstrip()) # [-1] because for loop is one ahead
            db[-1]['raw'].write(line)



def parse_fasta_binary_IO(file, db):
    file_handle = open(file, "rb")

    for line in file_handle:
        if line[0] == 62:
            description, id = line[1:].split(maxsplit=1) 
            db.append({'id': id,
                       'description': description,
                       'sequence': io.BytesIO(),
                       'raw': io.BytesIO()})
        else:
            db[-1]['sequence'].write(line.rstrip())
            db[-1]['raw'].write(line)









def take_time(func, args, **kwargs): #**kwargs ist für das Dictionary (keyworded arguments)
    start = time.time() #speichert die aktuelle Zeit in eine Variable (Sekunden seit epoch - 1.1.1970 0 Uhr 0:0)
    func(args, **kwargs)
    end = time.time()
    print("Function takes {:.3} seconds".format(end-start)) #hier wird auf drei Nachkommastellen reduziert









database = []

take_time(parse_fasta, "../examples/sequence.fasta", db=database) 
take_time(parse_fasta_binary, "../examples/sequence.fasta", db=database)

take_time(parse_fasta_IO, "../examples/sequence.fasta", db=database) 
take_time(parse_fasta_binary_IO, "../examples/sequence.fasta", db=database)



