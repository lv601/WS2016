from pprint import pprint

# TIPP: Packen Sie alles in eine Funktion, der Sie den Filenamen übergeben,
# dann können Sie den Code leicht mehrmals verwenden
def parse_fasta(file):
    file_handle = open(file, "r")

    db =[]
    for line in file_handle:
        # TIPP: Wenn Sie wie hier nur auf ein Zeichen prüfen, können Sie auch
        # den Indexoperator benutzen. Der ist schneller.
        if line[0] == ">":
        #if line.startswith(">"): #wenn das hier TRUE ist, dann wird ein neues Objekt erstellt und die anschließenden Sachen werden auf die weiteren Indices weiter gegeben
            id, description = line[1:].split(maxsplit=1) #aus beiden Teilen wird eine Variable erstellt; es wird genau einmal gesplittet
            db.append({'id': id, 'description': description, 'sequence': "", 'raw': line})
        else:
            db[-1]['sequence'] += line.rstrip()
            db[-1]['raw'] += line

    pprint(db)
    print(len(db))
parse_fasta("../examples/sequence.fasta")