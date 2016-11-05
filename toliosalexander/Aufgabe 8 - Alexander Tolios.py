### Aufgabe 8 - Alexander Tolios - last modified am 29.10.2016 ###

# Kopie von Aufgabe 6a:


db = [] # db wird leer erzeugt

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


# ab hier neuer Code


db_b = [] # db_b wird leer erzeugt

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
            db_b[-1]["sequence"]+= sequence  # Definiert Sequenzeintrag
            db_b[-1]["raw"]+= line   # Rohdaten (kompletter Eintrag)



import time

start = time.time()
fasta_parser(db, "../examples/long.fasta")
end = time.time()
par_str = (end-start)
print("Parser mit str: {:.2} Sekunden".format(end-start))

start = time.time()
fasta_parser_b(db_b, "../examples/long.fasta")
end = time.time()
par_b = (end-start)
print("Parser mit bytearray: {:.2} Sekunden".format(end-start))

print("Der Bytearray-Parser ist um {:.2} Sekunden schneller".format(par_str-par_b))