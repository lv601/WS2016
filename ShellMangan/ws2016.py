#"fast parser"
import time
import re
from pprint import pprint
import sys
import io

def parse_fasta(filestream, db):
    file_handle = io.open("sequence.fasta", "r")

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
                

def get_gc_content(db, index):
    seq = db[index]["sequence"]
    count = 0
    for ind, char in enumerate(seq):
        if (char == "A") or (char == "T"):
            continue
        else:
            count +=1
    content = count / (ind+1)
    content *= 100
    return content


#time add-on
def stop_time(func, *args,**kargs):
    start=time.time()
    result=func(*args, **kargs)
    end=time.time()
    print("Function {} takes {:.3} seconds".format(func.__name__,end-start))
    return result
d=[]
res1=stop_time(parse_fasta, "../examples/long.fasta",db=d)

if __name__=="__main__":
    print(__file__)
