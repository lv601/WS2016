def parse_fasta(file):
    file_handle = open(file, "r")
    db = None

    for line in file_handle:
        if line[0] == ">":
            if db: #return if db has an full entry
                yield db

            id, description = line[1:].split(maxsplit=1) #aus beiden Teilen wird eine Variable erstellt; es wird genau einmal gesplittet
            db = {'id': id, 'description': description, 'sequence': ""}
        else:
            db['sequence'] += line.rstrip()

    else:
        yield db


#Hier wird gleich alles ausgegeben
#for item in parse_fasta("../examples/sequence.fasta"):
#    print(item)

#hier wird immer nur der nächste Eintrag ausgegeben
test = parse_fasta("../examples/sequence.fasta")
next(test)