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
    file_handle = open(file_name, "r")
    file_handle = file_handle.encode('utf8')

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





start = time.time();
parse_fasta(d, "fasta.fa");
end = time.time()
print("{:.3} seconds".format(endstart))

