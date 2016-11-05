### Aufgabe 11 - Alexander Tolios - last modified am 29.10.2016 ###
# Subdatei fasta_parser


import io


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

db_bIO = [] # db_bIO wird leer erzeugt

# Aufruf der Funktion fasta_parser 
# fasta_parser_bIO(db_bIO, "../examples/sequence.fasta")


