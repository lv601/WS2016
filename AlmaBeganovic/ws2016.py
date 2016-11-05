import io
import sys

def fasta_parser(stream):
    
    if isinstance(stream.read(0), bytes):
        db = []
        for line in stream:
            if line[0] == 62: #
                header, desc = line.split(maxsplit=1)
                header = header[1:]
                desc = desc.strip()
                db.append({"id":header, "desc":desc, "raw":io.BytesIO(line), "sequence":io.BytesIO()})
            else:
                line = line.strip()
                db[-1]['sequence'].write(line)
                db[-1]['raw'].write(line)
        return(db)
    else:
        print("Der Stream muss binaer sein.", file=sys.stderr)
        exit(-1)


def get_raw(db, index):

    return db[index]['raw']

def get_id(db, index):

    return db[index]['id']

def get_description(db, index):

    return db[index]['desc']

def get_sequence(db, index):

    return db[index]['sequence']

def get_fasta(db, index, line_length=80):

    lines = []
    for i in range(0, (len(db[index]['sequence']) // line_length) * line_length, step=line_length):
        lines.append(db[index]['sequence'][i:i + line_length])
        if len(sequence) % line_length > 0:
            lines.append(sequence[i:])

        return "\n".join(lines)

def get_feature(db, index, feature):

    return(db[index][feature])

def add_feature(db, index, feature, value):

    db[index][feature] = value
    return db[index]

def add_sequence_object(db, id, description, sequence, **features):

    db.append({"id":id, "desc":description, "sequence":sequence, **features})
    return(db)

def get_gc_content(db, index):

    seq = db[index]["sequence"]
    count = 0
    for ind, char in enumerate(seq):
        if (char == "A") or (char == "T"):
            continue
        else:
            count +=1
    content = count / (ind+1)
    content *= 100
    return content

def get_output(db, index, type):

    if type == "markdown":
        output = "# H1" + db[index]["id"] + "*" + db[index]["desc"] + "*" + "\n" + "```" + db[index]["sequence"] + "```"
    elif type == "html":
        output = "<h1>" + db[index]["id"] + "</h1><i>" + db[index]["desc"] + "</i>" + "<br><br>" + "<code>" + db[index]["sequence"] + "</code>"
    else:
        output = db[index]["id"] + db[index]["desc"] + db[index]["sequence"]
    return output
