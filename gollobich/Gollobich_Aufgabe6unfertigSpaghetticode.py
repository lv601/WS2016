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

