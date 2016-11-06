#!/usr/bin/env python3

""" 
Aufgabe 6
Schreiben Sie eine Funktion, die ein Fasta File (WS2016/examples/sequence.fasta) einliest, parst und in ein Daten-Objekt
einfügt.

Siehe WS2016/exercises/aufgabe6.pdf
"""


import time

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
    file_handle = open(file_name, "br")

    for line in file_handle:
        if line[0] == 62: ### zahl da > nicht gelesen werden kann da bytes
            # New fasta sequence starts - parse header
            ident, desc = line[1:].strip().split(maxsplit=1)

            # Create new sequence entry in db
            db.append({'id': ident, 'description': desc,'sequence': bytearray(), 'raw': bytearray(line)})
        else:
            # Sequence line
            db[-1]['sequence'] += (line.rstrip())
            db[-1]['raw'] += (line)

# ACHTUNG: Einige Typos


data = []
parse_fasta(data, "sequence.fasta")
print(data)

start = time.time()
parse_fasta(data, "sequence.fasta")
end = time.time()
print("{:.3} seconds".format(end-start))



