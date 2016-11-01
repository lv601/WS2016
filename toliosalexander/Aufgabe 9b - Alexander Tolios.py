### Aufgabe 9b - Alexander Tolios - last modified am 29.10.2016 ###

import time, io

def fasta_parser (db, path):    # Funktion wird definiert
    file_handle = open(path, "r")  # "r" bedeutet read-only mode
    for line in file_handle:
        if line[0] == ">":  # Format: Kopfzeile beginnt immer mit >
            id, description = line.split(" ", maxsplit=1)    # Splitting erfolgt eim Leerzeichen, max. 1x
            id = id[1:] # Beginn der Zeile (>) wird entfernt
            description = description.strip() # entfernt Umbruch
            db.append({"id": id, "description": description, "sequence": "", "raw": line}) # fügt neuen Eintrag in DB hinzu
        else:
            sequence = line.strip()
            db[-1]["sequence"]+= sequence  # Definiert Sequenzeintrag
            db[-1]["raw"]+= line   # Rohdaten (kompletter Eintrag)

def fasta_parser_b (db_b, path):    # Funktion wird definiert
    file_handle = open(path, "rb")  # "rb" bedeutet read-only mode als bytearray
    for line in file_handle:
        if line[0] == 62:  # Format: Kopfzeile beginnt immer mit > ; CAVE: der ASCII-Code für > ist 62
            id, description = line.split(maxsplit=1)    # Splitting erfolgt eim Leerzeichen, max. 1x; CAVE: darf für bytearray nicht als " " angegeben werden
            id = id[1:] # Beginn der Zeile (>) wird entfernt
            description = description.strip() # entfernt Umbruch
            db_b.append({"id": id, "description": description, "sequence": bytearray(), "raw": line}) # fügt neuen Eintrag in DB hinzu: CAVE: hier muss "" ausgebessert werden zu bytearray()
        else:
            sequence = line.strip()
            db_b[-1]["sequence"] += sequence  # Definiert Sequenzeintrag
            db_b[-1]["raw"] += line  # Rohdaten (kompletter Eintrag)

def fasta_parser_sIO (db_sIO, path):    # Funktion wird definiert
    file_handle = open(path, "r")  # "r" bedeutet read-only mode
    for line in file_handle:
        if line[0] == ">":  # Format: Kopfzeile beginnt immer mit >
            id, description = line.split(maxsplit=1)    # Splitting erfolgt eim Leerzeichen, max. 1x
            id = id[1:] # Beginn der Zeile (>) wird entfernt
            description = description.strip() # entfernt Umbruch
            db_sIO.append({"id": id, "description": description, "sequence": io.StringIO(),"raw": io.StringIO(line)}) # fügt neuen Eintrag in DB hinzu: CAVE: IO muss hier definiert werden
        else:
            sequence = line.strip()
            db_sIO[-1]["sequence"].write(sequence)  # Definiert Sequenzeintrag; CAVE: ohne +=
            db_sIO[-1]["raw"].write(line)   # Rohdaten (kompletter Eintrag); CAVE: ohne +=

def fasta_parser_bIO (db_bIO, path):    # Funktion wird definiert
    file_handle = open(path, "rb")  # "rb" bedeutet read-only mode als bytearray
    for line in file_handle:
        if line[0] == 62:  # Format: Kopfzeile beginnt immer mit > ; CAVE: der ASCII-Code für > ist 62
            id, description = line.split(maxsplit=1)    # Splitting erfolgt eim Leerzeichen, max. 1x; CAVE: darf für bytearray nicht als " " angegeben werden
            id = id[1:] # Beginn der Zeile (>) wird entfernt
            description = description.strip() # entfernt Umbruch
            db_bIO.append({"id": id, "description": description, "sequence": io.BytesIO(),"raw": io.BytesIO(line)}) # fügt neuen Eintrag in DB hinzu: CAVE: bIO muss hier definiert werden
        else:
            sequence = line.strip()
            db_bIO[-1]["sequence"].write(sequence)  # Definiert Sequenzeintrag; CAVE: für IO ohne +=
            db_bIO[-1]["raw"].write(line)   # Rohdaten (kompletter Eintrag); CAVE: ohne +=

# Funktion: Zeit wird berechnet
def comp_time(func, *args, **kargs):
    start = time.time()
    result = func(*args, **kargs)
    end = time.time()
    print("Funktion {} braucht {:.2} Sekunden".format(func.__name__, end-start))
    return result


db = [] # db wird leer erzeugt
db_b = [] # db_b wird leer erzeugt
db_sIO = [] # db_sIO wird leer erzeugt
db_bIO = [] # db_bIO wird leer erzeugt

# Aufruf der Funktion fasta_parser in der Funktion comp_time, mit zugeordneter db und Quelle
comp_time(fasta_parser, db, "../examples/long.fasta") 
comp_time(fasta_parser_b, db_b, "../examples/long.fasta")
comp_time(fasta_parser_sIO, db_sIO, "../examples/long.fasta")
comp_time(fasta_parser_bIO, db_bIO, "../examples/long.fasta")
