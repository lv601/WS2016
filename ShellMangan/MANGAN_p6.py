import re
from pprint import pprint
#db = database, dict for info
def parse_fasta(db, file_name):
    infile=open(file_name,"r")

    for line in infile:
        if line[0]==">":
            ident, desc=line[1:].strip().split(maxsplit=1)
            db.append({"id":ident, "description":desc,"sequence":"","raw":line})
        else:
            db[-1]["sequence"]+= line.rstrip()
            db[-1]["raw"]+=line

                
def get_raw(db, index):
    return db[index]["raw"]

def get_id(db, index):
    return db[index]["id"]

def get_description(db, index):
    return db[index]["description"]

def get_sequence(db, index):
    return db[index]["sequence"]

def get_feature(db, index, feature):
    feature=input("Please list feature you would like to show: ")
    return db[index][feature]



def get_fasta(db, index):
    str=">"+db[index]["id"]+" "+db[index]["description"]+"\n"
    rows=divmod(len(db[index]["sequence"]),80)
    if rows[1]>0:
        r=rows[0]+1
    else:
        r=rows[0]
    for i in range(r):
        str+=db[index]["sequence"][i*80:i*80+80]+"\n"
    return str

def add_feature(db, **features):
    db.append({**features})

def add_sequence_object(db, id, description, sequence, **features):
    db.append({"id":id, "description":description,"sequence":sequence,**features})

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
         

if __name__=="__main__":
    db=[]
    parse_fasta(db,"../examples/sequence.fasta")
    #parse_gb(db,"sequence.gb")
#    pprint(db[20])
    print(db[0]["id"])
    print(get_raw(db, 5))
   # print(get_fasta(db, 20))
    add_sequence_object(db, "myid","mydescription","ATG-OLE", organism="Student",test=[1,2,3])
    pprint(db[0])
    print(db)
    
    
    
                        
    
