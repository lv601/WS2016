#!/usr/bin/env python3
import time

def parse_fasta1(file_name, db):
    file_handle = open(file_name, "r")  # Change mode to binary

    for line in file_handle:
      if line[0] == ">":  # bytes are stored as numbers
          # New fasta sequence starts - parse header
          ident, desc = line[1:].strip().split(maxsplit=1)

          # Create new sequence entry in db
          db.append({'id': ident,
                     'description': desc,
                     'sequence': "",
                     'raw': line})
      else:
          # Sequence line
          db[-1]['sequence'] += line.rstrip()
          db[-1]['raw'] += line

def parse_fasta2(file_name, db):
    file_handle = open(file_name, "rb")  # Change mode to binary

    for line in file_handle:
      if line[0] == 62:  # ord(">") bytes are stored as numbers
          # New fasta sequence starts - parse header
          ident, desc = line[1:].strip().split(maxsplit=1)

          # Create new sequence entry in db
          db.append({'id': ident,
                     'description': desc,
                     'sequence': bytearray(),  # Switch to bytearray
                     'raw': bytearray(line)})  # Switch to bytearray
      else:
          # Sequence line
          db[-1]['sequence'] += (line.rstrip())
          db[-1]['raw'] += (line)

# Stop time of function calls
def stop_time(func, *args, **kargs):
    start = time.time()

    result = func(*args, **kargs)

    end = time.time()
    print("Function {} takes {:.3} seconds".format(func.__name__, end - start))
    return result

d = []

res1 = stop_time(parse_fasta1, "../examples/long.fasta", db=d)
res2 = stop_time(parse_fasta2, "../examples/long.fasta", db=d)

# Compare both sequences
print(d[0]['sequence'] == d[1]['sequence'].decode())

