#Bsp 8
import time

def parse_fasta1(file_name, db):
    file_handle = open(file_name, "r")

    for line in file_handle:
      if line[0] == ">":
          ident, desc = line[1:].strip().split(maxsplit=1)
          db.append({"id": ident,
                     "description": desc,
                     "sequence": "",
                     "raw": line})
      else:
          db[-1]["sequence"] += line.rstrip()
          db[-1]["raw"] += line

def parse_fasta2(file_name, db):
    file_handle = open(file_name, "rb")

    for line in file_handle:
      if line[0] == ord(">"):
          ident, desc = line[1:].strip().split(maxsplit=1)
          db.append({"id": ident,
                     "description": desc,
                     "sequence": bytearray(),
                     "raw": bytearray(line)})
      else:
          db[-1]["sequence"] += (line.rstrip())
          db[-1]["raw"] += (line)


def stop_time(func, *args, **kargs):
    start = time.time()

    result = func(*args, **kargs)

    end = time.time()
    print("Function {} takes {:.3} seconds".format(func.__name__, end - start))
    return result

d = []

res1 = stop_time(parse_fasta1, "../examples/long.fasta", db=d)
res2 = stop_time(parse_fasta2, "../examples/long.fasta", db=d)

# Comparison
print(d[0]["sequence"] == d[1]["sequence"].decode())


