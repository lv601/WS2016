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


def calc_gc(db):
    print("_____________________\n")
    for item in db:
        c = item["sequence"].getvalue().count("C")
        g = item["sequence"].getvalue().count("G")
        ges = len(item["sequence"].getvalue())
        pro = (c + g)/ges * 100
        print("GC-Gehalt:", round(pro, 2), "%")
        print("GC-Gehalt:", round(pro, 4), "%")
        print("_____________________\n")
        return pro

database = []
parse_fasta(args.fasta, database)

calc_gc(database)
