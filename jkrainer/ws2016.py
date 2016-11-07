import time

def parse_fasta_binary(file):
    db = []

    for line in file:
        if line[0] == 62:
            description, id = line[1:].split(
                maxsplit=1)  # aus beiden Teilen wird eine Variable erstellt; es wird genau einmal gesplittet
            db.append({'id': id,
                       'description': description,
                       'sequence': bytearray(),
                       'raw': bytearray()})
        else:
            db[-1]['sequence'] += line.rstrip()
            db[-1]['raw'] += line

def parse_fasta(file_handle):
    db = []

    for line in file_handle:
        if line[0] == ">":
            description, id = line[1:].split(maxsplit=1) #aus beiden Teilen wird eine Variable erstellt; es wird genau einmal gesplittet
            db.append({'id': id,
                       'description': description,
                       'sequence': "",
                       'raw': line})
        else:
            db[-1]['sequence'] += line.rstrip()
            db[-1]['raw'] += line

def parse_fasta_gc(file):
    db = []

    for line in file:
        if line[0] == 62:
            description, id = line[1:].split(maxsplit=1)  # aus beiden Teilen wird eine Variable erstellt; es wird genau einmal gesplittet
            db.append({'id': id,
                       'description': description,
                       'sequence': bytearray(),
                       'raw': bytearray()})
        else:
            db[-1]['sequence'] += line.rstrip()
            db[-1]['raw'] += line

def take_time(func, args): #**kwargs ist für das Dictionary (keyworded arguments)
    start = time.time() #speichert die aktuelle Zeit in eine Variable (Sekunden seit epoch - 1.1.1970 0 Uhr 0:0)
    func(args)
    end = time.time()
    print("Function takes {:.3} seconds".format(end-start)) #hier wird auf drei Nachkommastellen reduziert