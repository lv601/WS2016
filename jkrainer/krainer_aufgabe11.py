import io
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-f", "--fasta", help="fasta file")

args = parser.parse_args()

def parse_fasta(file, db):
    file_handle = open(file, "r")

    for line in file_handle:
        if line[0] == ">":
            description, id = line[1:].strip().split(maxsplit=1)

            db.append({'id': id,
                       'description': description,
                       'sequence': io.StringIO(),
                       'raw': io.StringIO(line)})
        else:
            db[-1]['sequence'].write(line.rstrip())
            db[-1]['raw'].write(line)

database = []
parse_fasta(args.fasta, database)

print(database[0]['sequence'].getvalue())
