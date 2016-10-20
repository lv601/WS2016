#! /usr/bin/env python3

""" Aufgabe 15
Ändern Sie die Fasta Parser Funktion aus Aufgabe 6 zu einer Generator Funktion um, die anstatt alle Sequenzen in einer
Liste zu speichern nur jeweils die einzelene Sequenz zurückgibt.

Vorteil dieser Version ist, dass wirklich immer nur eine Sequenz im Speicher gehalten wird und trotzdem einfach
verwendbar bleibt. Somit kann man auch Sequenz Files mit mehreren GBs problemlos verarbeiten.

for seq in parse_fasta(file_name):
    print(seq['id'], seq['desc'], len(seq['seq']))
"""
def parse_fasta(file_name):
    """
    Parse a multi sequence fasta file and map it to a dictionary
    :param file_name:
    :return: None
    """
    file_handle = open(file_name, "r")

    db = None

    for line in file_handle:
        if line[0] == ">":
            if db:
                yield db
                db = None

            # New fasta sequence starts - parse header
            ident, desc = line[1:].strip().split(maxsplit=1)

            # Create new sequence entry in db
            db = {'id': ident, 'desc': desc, 'seq': "", 'raw': line}
        else:
            # Sequence line
            db['seq'] += line.rstrip()
            db['raw'] += line
    else: # End of for loop
        # Returns last entry when 'for line in file_handle:' is not called anymore
        yield db


for seq in parse_fasta("../examples/long.fasta"):
    print(seq['id'], seq['desc'], "\nSeq. Length: {}".format(len(seq['seq'])))