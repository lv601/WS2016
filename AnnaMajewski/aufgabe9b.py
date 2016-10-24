## Date: 18.10.2016
## Author: Anna Majewski
## Description: Aufgabe 8 ueberarbeiten, sodass String.IO und Bytes.IO
## verwendet werden und ueberpruefen welche Funktion schneller ist.

# Import der libraries io und time
import io, time

# Fasta Parser 3 verwendet String.IO

def fasta_parser3(filename):
    """fasta parser, reads fasta file and introduces content into list"""
    file_handle = open(filename, "r")
# Öffnet eine Datei in read mode, binär
    for index, line in enumerate(file_handle):
## > leitet die Zeile ein, 62 in ascii
        if line[0] == ">":
# stattdessen mit .split geteilt
            header, desc = line.split(maxsplit=1)
            header = header[1:]
            desc = desc.strip()
            if index == 0:
# Eine Datenbank wird erstellt. Leere Felder erhalten bytearray() statt ""
                db = [{"id": header, "desc": desc, "sequence": io.StringIO(), "raw": io.StringIO(line)}]
            else:
# In die vorhandene Datenbank wird ein neuer Eintrag eingefügt.
                db.append({"id":header, "desc":desc, "raw":io.StringIO(line), "sequence":io.StringIO()})
        else:
            line = line.strip()
            db[-1]['sequence'].write(line)
            db[-1]['raw'].write(line)
    return(db)

#################################

# Fasta Parser 4 verwendet Bytes.IO

def fasta_parser4(filename):
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
# Eine Datenbank wird erstellt. Leere Felder erhalten bytearray() statt ""
                db = [{"id": header, "desc": desc, "sequence": io.BytesIO(), "raw": io.BytesIO(line)}]
            else:
# In die vorhandene Datenbank wird ein neuer Eintrag eingefügt.
                db.append({"id":header, "desc":desc, "raw":io.BytesIO(line), "sequence":io.BytesIO()})
        else:
            line = line.strip()
            db[-1]['sequence'].write(line)
            db[-1]['raw'].write(line)
    return(db)

## Aufgabe 2: Zeit messen und vergleichen

start = time.time()
fasta_parser3("../examples/long.fasta")
end = time.time()
print("Dauer des Parsens mit StringIO: {:.3} Sekunden".format(end-start))

start = time.time()
fasta_parser4("../examples/long.fasta")
end = time.time()
print("Dauer des Parsens mit BytesIO: {:.3} Sekunden".format(end-start))

# Ich imortiere die datei aufgabe8.py um den Vergleich zwischen allen 4 Parsern zu ziehen.
import aufgabe8

# Man sieht, dass der schnellste Parser BytesIO ist.
# Für die weiteren Beispiele werde ich deshalb mit Parser 4 arbeiten.
