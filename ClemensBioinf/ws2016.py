## Aufgabe 11 ##

def fasta_parser(user_input):
    data = []
    total_raw = ""
    for line in user_input:
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

    #print(data)
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


if __name__ == '__main__':
    print(__file__)
