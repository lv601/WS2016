### Aufgabe 6a - Alexander Tolios - last modified am 29.10.2016 ###

# Informationen nauer: 
# Schreiben Sie eine Funktion, die ein Fasta File (WS2016/examples/sequence.fasta) einliest, parst und in ein Daten-Objekt einfügt.
# Siehe WS2016/exercises/aufgabe6.pdf



db = [] # db wird leer erzeugt

def fasta_parser (db, path):    # Funktion wird definiert
    file_handle = open(path, "r")  # "r" bedeutet read-only mode
    for line in file_handle:
        if line[0] == ">":  # Format: Kopfzeile beginnt immer mit >
            id, description = line.split(" ", maxsplit=1)    # Splitting erfolgt eim Leerzeichen, max. 1x
            id = id[1:] # Beginn der Zeile (>) wird entfernt
            description = description.strip() # entfernt Umbruch
            db.append({"id": id, 
                       "description": description, 
                       "sequence": "", 
                       "raw": line}) # fügt neuen Eintrag in DB hinzu
        else:
            sequence = line.strip()
            db[-1]["sequence"]+= sequence  # Definiert Sequenzeintrag
            db[-1]["raw"]+= line   # Rohdaten (kompletter Eintrag)

fasta_parser(db, "../examples/short.fasta")

