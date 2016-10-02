#Aufgabe 8
#ändere den fasta parser v. Aufgabe 6
#anstatt str soll bytearray verwendet werden
#geschwindigkeitstest mit time machen
import time
import re
from pprint import pprint

def parse_fasta(file_name, db):
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
    db=[]
    parse_fasta(db,"sequence.fasta")
    parse_gb(db,"sequence.gb")
    pprint(db[20])
    print(db[0]["id"])
    print(get_raw(db, 5))
    print(get_fasta(db, 20))
    add_sequence_object(db, "myid","mydescription","ATG-OLE", organism="Student",test=[1,2,3])
    pprint(db[0])
    print(db)
