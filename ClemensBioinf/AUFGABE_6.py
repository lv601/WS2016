def fasta_parser(path):
    data = []
    total_raw = ""
    for line in open(path, "r"):
        total_raw += line

    for sequence in total_raw.split(">")[1:]:
        header = True
        curr_seq = {}
        curr_seq["raw"] = ""
        curr_seq["sequence"] = ""
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
        collect_notes = False
        for line in entry.split("\n"):
            if "".join(line.split(" ")[0]) != "":
                curr_attribute = "".join(line.split(" ")[0])
            if curr_attribute == "VERSION":
                curr_entry["id"] = line.split(" ")[7] + "|" + line.split(" ")[5]
                curr_entry["id"] = "gi|" + curr_entry["id"][3:]
            elif curr_attribute == "DEFINITION":
                curr_entry["description"] = line.lstrip("DEFINITION").strip(" ")
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
                    curr_entry["features"]["id"] = line.lstrip('                     /db_xref="').rstrip('"')

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
    for char in db[index]["id"] + "| " + db[index]["description"]:
        char_count += 1
        if char_count % 80 == 0:
            header += "\n"
        header += char

    char_count = -1
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

def add_sequence_object(db, id, description, sequence, **features):
    db.append({"id":id, "description":description, "sequence":sequence, "features":features})

def get_gc_content(db, index):
    seq = db[index]["sequence"]
    count_gc = 0
    count_all = 0
    for char in seq:
        if char == "g" or char == "c":
            count_gc += 1
        count_all += 1

    return str(round(count_gc / count_all, 5) * 100) + " %"

def get_output(db, index, type='markdown'):
    pass


# fasta_parser("/home/vortex/Desktop/Bioinformatik/Programmieren/WS2016/examples/sequence.fasta")
db = genbank_parser("/home/vortex/Desktop/Bioinformatik/Programmieren/WS2016/examples/sequence.gb")
#add_sequence_object(db, "testid", "test desc", "atgc", feature1="featureA", feature2="featureB")
print(get_gc_content(db, 0))