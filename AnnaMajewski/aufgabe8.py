## Date: 27.09.2016
## Author: Anna Majewski
## Description: Parser für FASTA-files, bytearry statt str

from pprint import pprint

## ALTER PARSER # hier keine Veränderungen vorgenommen, wie in aufgabe6.py

def fasta_parser(filename):
    """fasta parser, reads fasta file and introduces content into list"""
    file_handle = open(filename, "r")
# Öffnet eine Datei in read mode
    position = 0
    for index, line in enumerate(file_handle):
# Index, weil für den ersten Eintrag eine Datenbank erstellt werden muss.
        # TIPP: In dem Fall, dass nur ein Zeichen geprüft wird, können Sie auch
        # einfach den Indexoperator verwenden. Der ist schneller.
        # in Ordnung:
        if line[0] == ">":
        #if line.startswith(">"):
            line = line.strip()
            # TIPP: Das geht einfacher mit .split() oder .partition(" ")
            position = line.index(" ")
            header = line[0:position-1]
            desc = line[position+1:]
# Da erstes " " als Trennung zwischen Header und Beschreibung gilt,
# zuerst bis position von " " = header, alles danach = description.
            if index == 0:
# Eine Datenbank wird erstellt.
                db = [{"id": header, "desc": desc, "sequence": "", "raw": line}]
            else:
# In die vorhandene Datenbank wird ein neuer Eintrag eingefügt.
                db.append({"id":header, "desc":desc, "raw":line, "sequence":""})
        else:
            line = line.strip()
            db[-1]['sequence'] += line
            db[-1]['raw'] += line
    return(db)

## NEUER PARSER # hier etwas angepasst und die Tipps beherzigt!

def fasta_parser2(filename):
    """fasta parser, reads fasta file and introduces content into list"""
    file_handle = open(filename, "rb")
# Öffnet eine Datei in read mode, binär
    for index, line in enumerate(file_handle):
## > leitet die Zeile ein, 62 in ascii
        if line[0] == 62:
# stattdessen mit .split geteilt
            header, desc = line.split(maxsplit=1)
            header = header[1:]
            desc = desc.strip()
            if index == 0:
# Eine Datenbank wird erstellt. Leere Felder erhalten bytearry() statt ""
                db = [{"id": header, "desc": desc, "sequence": bytearray(), "raw": line}]
            else:
# In die vorhandene Datenbank wird ein neuer Eintrag eingefügt.
                db.append({"id":header, "desc":desc, "raw":line, "sequence":bytearray()})
        else:
            line = line.strip()
            db[-1]['sequence'] += line
            db[-1]['raw'] += line
    return(db)


## 2. Aufgabe, Zeit messen mit time.time

import time

start = time.time()
fasta_parser("../examples/sequence.fasta")
end = time.time()
print("Dauer des Parsens mit Strings: {:.3} Sekunden".format(end-start))

start = time.time()
fasta_parser2("../examples/sequence.fasta")
end = time.time()
print("Dauer des Parsens mit Bytearray: {:.3} Sekunden".format(end-start))
