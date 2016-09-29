from time import time

def fasta_parser(path):
    data = []
    total_raw = ""
    for line in open(path, "r"):
        total_raw += line

    for sequence in total_raw.split(">")[1:]:
        header = True
        curr_seq = {}
        # TIPP: Hier könnten Sie gleich sequence übergeben
        # curr_seq["raw"] = sequence
        curr_seq["raw"] = ""
        curr_seq["sequence"] = ""

        # TIPP: Da Header immer in der ersten Zeile steht, könnten Sie den Code
        # folgendermaßen umformen um zeitfressende Abfragen zu vermeiden.
        # lines = sequence.split("\n") oder besser lines = sequence.splitlines()
        # header = sequence.partition(" ")
        # curr_seq["id"] = header[0]
        # curr_seq["desc"] = header[2] Vermeidet Error falls Header keine description enthält
        for line in sequence.split("\n"):
            if header is True:
                curr_seq["id"] = line.split(" ")[0]
                curr_seq["description"] = " ".join(line.split(" ")[1:])
                header = False
            else:
                curr_seq["sequence"] += line

            curr_seq["raw"] += line

        data.append(curr_seq)

    return data

def genbank_parser(path):
    data = []
    total_raw = ""
    for line in open(path, "r"):
        total_raw += line

    for entry in total_raw.split("//")[:-1]:
        curr_attribute = ""
        curr_entry = {}
        curr_entry["raw"] = ""
        curr_entry["sequence"] = ""
        curr_entry["features"] = {}
        curr_entry["features"]["description"] = ""
        curr_entry["description"] = ""
        collect_notes = False
        for line in entry.split("\n"):
            if "".join(line.split(" ")[0]) != "":
                curr_attribute = "".join(line.split(" ")[0])
            if curr_attribute == "VERSION":
                curr_entry["id"] = line.split(" ")[7] + "|" + line.split(" ")[5]
                curr_entry["id"] = "gi|" + curr_entry["id"][3:]
            elif curr_attribute == "DEFINITION":
                curr_entry["description"] += (" ".join(line.lstrip("DEFINITION").strip(" ").split("\n"))) + " "
            elif curr_attribute == "ORIGIN":
                raw_seq = line.lstrip("ORIGIN")
                seq = ""
                for char in raw_seq:
                    if char in ["a", "t", "g", "c"]:
                        seq += char
                curr_entry["sequence"] += seq
            elif curr_attribute == "SOURCE":
                if line.split(" ")[0] == "SOURCE":
                    curr_entry["organism"] = line.split(" (")[0].lstrip("SOURCE").lstrip(" ")
            elif curr_attribute == "FEATURES":
                if "     gene            " in line:
                    curr_entry["features"]["position"] = line.lstrip("     gene            ")
                elif "/gene=" in line:
                    curr_entry["features"]["name"] = line.lstrip('                     /gene="').rstrip('"')
                elif "/note=" in line or collect_notes is True:
                    if collect_notes is True and '"' in line: # Letzte Zeile in "/note" erreicht
                        collect_notes = False
                    else:
                        collect_notes = True
                    curr_entry["features"]["description"] += line.lstrip('                     /note="').rstrip('"')+" "
                elif "/db_xref=" in line:
                    curr_entry["features"]["gene_id"] = line.lstrip('                     /db_xref="').rstrip('"')\
                        .lstrip("GeneID:")

            curr_entry["raw"] += line

        data.append(curr_entry)
    return data


def get_raw(db,	index):
    return db[index]["raw"]

def get_id(db, index):
    return db[index]["id"]

def get_description(db,	index):
    return db[index]["description"]

def get_sequence(db, index):
    return db[index]["sequence"]

def get_fasta(db, index):
    header = ""
    seq = ""
    char_count = 0

    # Die 80 Zeichen Grenze gilt für Fasta Header nicht. Das File wäre nicht
    # mehr valide, wenn der Header über 2 Zeilen geht. Konnten Sie nicht wissen
    for char in db[index]["id"] + "| " + db[index]["description"]:
        char_count += 1
        if char_count % 80 == 0:
            header += "\n"
        header += char

    char_count = -1
    # UGH: Sie loopen über jedes Zeichen in der Sequenz, dass kostet viel Zeit.
    # Verwenden Sie lieber den Indexoperator mit dem range der Zeilenlänge
    # lines = []
    # for i in range(0, (len(sequence) // line_length) * line_length, step=line_length):
    #     lines.append(sequence[i:i + line_length])
    #
    # if len(sequence) % line_length > 0:
    #     lines.append(sequence[i:])
    for char in db[index]["sequence"]:
        char_count += 1
        if char_count % 80 == 0:
            seq += "\n"
        seq += char

    return header + seq

def get_feature(db, index, feature):
    return db[index]["features"][feature]

def add_feature(db, index, feature, value):
    db[index]["features"][feature] = value
    return db

def add_sequence_object(db, id, description, sequence, **features):
    db.append({"id":id, "description":description, "sequence":sequence, "features":features})
    return db

def get_gc_content(db, index):
    seq = db[index]["sequence"].lower()
    return str(round((seq.count("c") + seq.count("g")) * 100 / len(seq),2)) + "%"

def get_output(db, index, type="markdown"):
    if type == "markdown":
        output_features = ""
        for feature in db[index]["features"].keys():
            output_features += "* " + feature.upper() + ": " + db[index]["features"][feature] + "\n"
        return "#__" + db[index]["features"]["name"] + ": " + db[index]["id"].split("|")[2] + "__\n" + \
               "##" + db[index]["description"] + "\n\n" + "__Features:__\n" + output_features + "\n---\n" + \
               "__Sequence__:\n" + db[index]["sequence"] + "\n\n---"
    elif type == "csv": # Verbesserungswürdig. Seperator = ~
        attributes = ""
        attribute_content = ""
        for attribute in db[index].keys():
            if attribute == "features":
                for feature in db[index]["features"].keys():
                    attributes += feature.upper() + "~"
                    attribute_content += db[index]["features"][feature] + "~"
            else:
                attributes += attribute.upper() + "~"
                attribute_content += db[index][attribute] +  "~"
        return attributes + "\n" + attribute_content


start = time()
fasta_parser("../examples/sequence.fasta")
end = time()
print("Total time: {}".format(round(end-start, 5)))
#db = genbank_parser("../examples/sequence.gb")
