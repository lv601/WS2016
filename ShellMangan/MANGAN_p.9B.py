import io
import time

def parse_fasta3(file_name, db):
    file_handle = open(file_name, "r")

    for line in file_handle:
        if line[0] == ">":
            ident, desc = line[1:].strip().split(maxsplit=1)

            db.append({"id": ident,
                       "description": desc,
                       "sequence": io.StringIO(),
                       "raw": io.StringIO(line)})
        else:
            db[-1]["sequence"].write(line.rstrip())
            db[-1]["raw"].write(line)

def parse_fasta4(file_name, db):
    file_handle = open(file_name, "rb")

    for line in file_handle:
        if line[0] == 62:
            ident, desc = line[1:].strip().split(maxsplit=1)
            db.append({"id": ident,
                       "description": desc,
                       "sequence": io.BytesIO(),
                       "raw": io.BytesIO(line)})
        else:
            db[-1]["sequence"].write(line.rstrip())
            db[-1]["raw"].write(line)

def stop_time(func, *args, **kargs):
    start = time.time()
    result = func(*args, **kargs)
    end = time.time()
    print("Function {} takes {:.3} seconds".format(func.__name__, end - start))
    return result

d = []

res3 = stop_time(parse_fasta3, "../examples/long.fasta", db=d)
res4 = stop_time(parse_fasta4, "../examples/long.fasta", db=d)
