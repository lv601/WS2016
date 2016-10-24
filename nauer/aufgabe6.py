#!/usr/bin/env python3

""" Aufgabe 6
Schreiben Sie eine Funktion, die ein Fasta File (WS2016/examples/sequence.fasta) einliest, parst und in ein Daten-Objekt
einfügt.

Schreiben Sie eine Funktion, die ein Genbank File (WS2016/examples/sequence.gb) einliest, parst und in ein Daten-Objekt
einfügt.

Siehe WS2016/exercises/aufgabe6.pdf
"""

import re
from pprint import pprint

# db [{seq1}, {seq2}, {seq3}, ...] Sequence of dictionaries

def parse_fasta(db, file_name):
    """
    Parse a multi sequence fasta file and map it to a dictionary
    :param db:
    :param file_name:
    :return: None
    """
    file_handle = open(file_name, "r")

    for line in file_handle:
        if line[0] == ">":
            # New fasta sequence starts - parse header
            ident, desc = line[1:].strip().split(maxsplit=1)

            # Create new sequence entry in db
            db.append({'id': ident, 'description': desc, 'sequence': "", 'raw': line})
        else:
            # Sequence line
            db[-1]['sequence'] += line.rstrip()
            db[-1]['raw'] += line


def parse_gb(db, file_name):
    """
    Parse a multi sequence genbank file and map it to a dictionary

    The main loop runs first. It seperates the genbank sequences. Then the secondary loop seperates different fields in
    the genbank sequence
    :param db:
    :param file_name:
    :return: None
    """
    file_handle = open(file_name, "r")

    # Needed for fields longer than one line
    store = None

    # Main loop for each sequence
    for line in file_handle:
        # New genbank sequence starts
        if line.startswith("LOCUS"):
            # Create new sequence entry in db
            db.append({'raw': line})

            # Loop for sequence content
            for line2 in file_handle:
                db[-1]['raw'] += line2  # [-1] last item in sequence

                # If field has more lines
                if store:
                    if line2.startswith(" " * 6):  # = 6 spaces - feature names have 5 spaces indent
                        store[0][store[1]] += line2.strip()
                    else:
                        store = None  # Reset store

                # Parse ACCESSION field (id)
                if line2.startswith("ACCESSION"):
                    db[-1]['id'] = line2.strip().split(maxsplit=1)[1]

                # Parse ORGANISM field
                if line2.startswith("  ORGANISM"):
                    db[-1]['organism'] = line2.strip().split(maxsplit=1)[1]

                # Parse DEFINITION field (description)
                if line2.startswith("DEFINITION"):
                    db[-1]['description'] = line2.strip().split(maxsplit=1)[1]

                    # Field has more than one line
                    store = (db[-1], "description")

                # Parse ORIGIN field (sequence)
                if line2.startswith("ORIGIN"):
                    db[-1]['sequence'] = ""

                    # Field has more than one line
                    store = (db[-1], "sequence")

                # Parse nested genes
                if line2.startswith("     gene"):
                    if "genes" in db[-1]:
                        db[-1]['genes'].append({'raw': line2.strip().split()[1]})
                    else:
                        # Create new nested gene dictionary
                        db[-1]['genes'] = [{'raw': line2.strip().split()[1]}]

                    # Field has more than one line
                    store = (db[-1]['genes'][-1], "raw")

                # Stop entry - leave inner loop
                if line2.startswith("//"):
                    # Tidy up sequence with regular expression
                    db[-1]['sequence'] = re.sub('\d*', "", db[-1]['sequence'])  # remove digits
                    db[-1]['sequence'] = re.sub('\s*', "", db[-1]['sequence'])  # remove whitespace

                    # Parse nested gene with helper function
                    _parse_gene(db[-1]['genes'][-1])
                    break # Leave loop


def _parse_gene(gene_str):  # Use _ for only internal functions
    """
    Helper function for nested gene parsing
    Split gene_str by / and add fields to data dictionary

    :param gene_str:
    :return: None
    """
    split = gene_str['raw'].split("/")
    gene_str['position'] = split.pop(0)

    for field in split:
        field, value = field.split("=")
        gene_str[field] = value


def get_raw(db, index):
    """
    Return original text data
    :param db:
    :param index:
    :return: str
    """
    return db[index]['raw']


def get_fasta(db, index, line_length=80):
    """
    Return sequence in fasta format
    :param db:
    :param index:
    :return: str
    """
    strings = [">{0[id]}|{0[description]}".format(db[index])]

    for i in range(0, len(db[index]['sequence']), line_length):
        strings.append(db[index]['sequence'][i:i + line_length])

    return "\n".join(strings)


def add_sequence_object(db, id, description, sequence, **features):
    """
    Add a new sequence to data dictionary
    :param db:
    :param id:
    :param description:
    :param sequence:
    :param features: Any kind of feature not mentioned in the main features
    :return: None
    """
    db.append({'id': id, 'description': description, 'sequence': sequence, **features})


# Run this part only if not imported
# Test library
if __name__ == "__main__":
    db = []

    parse_fasta(db, "../examples/sequence.fasta")

    parse_gb(db, "../examples/sequence.gb")

    pprint(db[20])
    print(db[0]['id'])

    print(get_raw(db, 5))

    print(get_fasta(db, 20))

    # Returns Doc string of function
    print(get_fasta.__doc__)

    add_sequence_object(db, "myid", "mydescription", "ATG-OLE", organism="Student", test=[1, 2, 3])

    pprint(db[0])

    print(db)
