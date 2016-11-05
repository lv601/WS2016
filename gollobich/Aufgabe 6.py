# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:41:57 2016

@author: lv
"""
import pprint

printer = pprint.PrettyPrinter()

raw = ""


def parse_fasta(db):
    file_handle = open("/home/lv/Documents/WS2016/examples/sequence.fasta", "r")
    
    obj = {}
    for line in file_handle:
        line = line.strip()
        # TIPP: Wenn Sie wie hier nur auf ein Zeichen prüfen, können Sie auch
        # den Indexoperator benutzen. Der ist schneller.
        # if zeile[0] == ">":
        if line.startswith('>'):
            if obj:
                db.append(obj)
            obj["sequence"]=""
            obj["raw"]=""
            obj["id"], obj["description"] = line.split(" ", 1)
            obj["id"] = obj["id"][1:]
        else:
            obj["sequence"] += line

        # ACHTUNG: line wurde bereits verändert 'line.strip()'
        # und ist nicht mehr raw. Verschieben Sie die Zeile
        # nach ganz oben im Loop
        obj["raw"] += line
            

        
db = []
parse_fasta(db)
#print(db)

def parse_genBank(dbgen):
    file_handle = open("/home/lv/Documents/WS2016/examples/sequence.gb", "r")
    
    obj = {}
    current_field = ""
    for line in file_handle:
        line = line.strip()
        if line.startswith('LOCUS'):
            if obj:
                dbgen.append(obj)
                obj = {}
                
            obj["raw"]=""
            
        if line.startswith("//"):
            current_field = ""
            
            
        if line.startswith('ORIGIN'):
            obj["sequence"]=""
            current_field="ori"
        elif current_field is "ori":
            sequences = line.split()[1:]
            sequence = "".join(sequences)           
            obj["sequence"] += sequence  
               
        if line.startswith('gene') and current_field is not "note":
            current_field="gene"
            
            obj["features"] = []
            
            feature = {}
            feature["position"] = line.split(maxsplit=1)[-1]
            
            obj["features"].append(feature)



        elif line.startswith('/gene') and current_field is "gene":
            name = line.split("=",maxsplit=1)[-1]
            feature["name"] = name.strip("\"")
    
        elif line.startswith('/note') and current_field is "gene":
            current_field = "note"
            note = line.split("=",maxsplit=1)[-1]
            feature["note"] = note.strip("\"")
            
        elif line.startswith('/db_xref') and (current_field is "note" or current_field is "gene"):
            current_field = "gene"
            id = line.split('/db_xref="')[-1]
            feature["id"] = id.strip('"')
        elif current_field is "note":
            feature["note"] += line
        
        if line.startswith('ORGANISM'):
            current_field = "org"
            obj["organism"] = line.split(maxsplit=1)[-1]
            
        if line.startswith('ACCESSION'):
            current_field = "acc"
            obj["id"] = line.split()[-1]
            
            
        if line.startswith('DEFINITION'): 
            obj["description"] = line.split(maxsplit=1)[-1]
            current_field = "def"
        elif current_field is "def":
           obj["description"] += line.strip()
        
dbgen = []
parse_genBank(dbgen)
printer.pprint(dbgen)


#Funktionen:

def get_raw(db, index):
    """reads database and returns field 'raw'"""
    return db[index]['raw']

def get_id(db, index):
    """reads database and returns field 'id' """
    return db[index]['id']

def get_description(db, index):
    """reads database and returns field 'description' """
    return db[index]['desc']

def get_sequence(db, index):
    """reads database and returns field 'sequence' """
    return db[index]['sequence']

def get_fasta(db, index, line_length=80):
    """reads database and returns fasta file with max. 80 chars in line"""
    lines = []
    for i in range(0, (len(db[index]['sequence']) // line_length) * line_length, step=line_length):
        lines.append(db[index]['sequence'][i:i + line_length])
        if len(sequence) % line_length > 0:
            lines.append(sequence[i:])

        return "\n".join(lines)

def get_feature(db, index, feature):
    """reads database and returns any field given """
    return(db[index][feature])

def add_feature(db, index, feature, value):
    """reads database and adds any given feature into database"""
    db[index][feature] = value
    return db[index]

def add_sequence_object(db, id, description, sequence, **features):
    """reads database and adds new entry into database"""
    db.append({"id":id, "desc":description, "sequence":sequence, **features})
    return(db)

def get_gc_content(db, index):
    """reads database and returns GC content of the sequence in % """
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

def get_output(db, index, type):
    """reads database and returns a desired output in html, markdown  or standard"""
    if type == "markdown":
        output = "# H1" + db[index]["id"] + "*" + db[index]["desc"] + "*" + "\n" + "```" + db[index]["sequence"] + "```"
    elif type == "html":
        output = "<h1>" + db[index]["id"] + "</h1><i>" + db[index]["desc"] + "</i>" + "<br><br>" + "<code>" + db[index]["sequence"] + "</code>"
    else:
        output = db[index]["id"] + db[index]["desc"] + db[index]["sequence"]
    return output
