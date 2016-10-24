#!/usr/bin/env python3

## Date: 29.09.2016 - 19.10.2016
## Author: Anna Majewski
## Description: Modul, das wir immer weiter erweitern

## Beschreibung des Codes // hier wird immer wieder upgedatet.
#1. Aufgabe 11: Zuerst Einfuegen des schnellsten Parsers. In meinem Fall ist das bytesIO Parser.
# Dann Bearbeiten, sodass Eingabe kein Filename sondern stream ist.
# Hinzufuegen von Test-Code, damit man sieht ob library direkt ausgefuehrt wird.

#2. Aufgabe 11: Alle weiteren Funktionen aus Uebung 6 eingefuegt und zur besseren Lesbarkeit,
# die Kommentare entfernt (Kommentare weiterhin in aufgabe6.py zu finden.
# Die Funktion get_fasta wurde nach den Tipps von nauer verbessert.

import io
import sys

def fasta_parser(stream):
    """fasta parser, reads fasta file and introduces content into list"""
    if isinstance(stream.read(0), bytes):
        db = []
        for line in stream:
            if line[0] == 62: ## > leitet die Zeile ein, 62 in ascii
                header, desc = line.split(maxsplit=1)
                header = header[1:]
                desc = desc.strip()
                db.append({"id":header, "desc":desc, "raw":io.BytesIO(line), "sequence":io.BytesIO()})
            else:
                line = line.strip()
                db[-1]['sequence'].write(line)
                db[-1]['raw'].write(line)
        return(db)
    else:
        print("Der Stream muss binaer sein.", file=sys.stderr)
        exit(-1)

## WEITERE FUNKTIONEN

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

## TESTCODE

if __name__ == "__main__":
# Run test code
    print(__file__)
