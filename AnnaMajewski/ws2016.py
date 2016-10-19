#!/usr/bin/env python3

## Date: 29.09.2016 - 19.10.2016
## Author: Anna Majewski
## Description: Modul, das wir immer weiter erweitern

import io

# zuerst einfuegen des schnellsten Parsers (bytesIO Parser)
# dann bearbeiten, dass Eingabe kein filename sondern bereits stream ist.

def fasta_parser(stream):
    """fasta parser, reads fasta file and introduces content into list"""
    if isinstance(stream.read(0), io.BytesIO):
        for line in stream:
            if line[0] == 62: ## > leitet die Zeile ein, 62 in ascii
                header, desc = line.split(maxsplit=1)
                header = header[1:]
                desc = desc.strip()
                if db:
                    # In die vorhandene Datenbank wird ein neuer Eintrag eingefügt.
                    db.append({"id":header, "desc":desc, "raw":io.BytesIO(line), "sequence":io.BytesIO()})
                else:
                    # Eine Datenbank wird erstellt. Leere Felder erhalten bytearray() statt ""
                    db = [{"id": header, "desc": desc, "sequence": io.BytesIO(), "raw": io.BytesIO(line)}]
            else:
                line = line.strip()
                db[-1]['sequence'].write(line)
                db[-1]['raw'].write(line)
        return(db)
    else:
        print("Stream must be opened as binary", file=sys.stderr)
            # Exit script with -1. Signals an error to the operationg system
        exit(-1)
