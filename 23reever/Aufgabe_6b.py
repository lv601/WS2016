# in GB File: raw (Original), id (ACCESSION), description (DEFINITION), sequence (ORIGIN), neues Feld features,
# alle gene einträge in eine Sequenz aus Dicts mit den Keys: position, name, description, id

def parse_def(file_hanlde, firstline):
    definition = firstline.replace("DEFINITION", "")
    definition = definition.strip()

    for i in file_hanlde:
        if i.startswith(" "):
            definition += i.strip()
        else:
            return definition,i

def parse_origin(file_handle):
    origin = ""
    for i in file_handle:
        if i.startswith(" "):
            i = i.strip()
            first = 1
            for j in i.split(" "):
                if not first:
                    origin += j
                else:
                    first = 0
        else:
            return origin,i

def parse_gene(file_handle, firstline):
    geneDict = {}
    position = firstline.replace("     gene", "")
    position = position.strip()
    geneDict["position"] = position
    #print(position)
    for i in file_handle:
        if i.startswith("      "):
            i = i.strip()
            if i.startswith("/gene"):
                i = i.replace("/gene=", "")
                i = i.replace("\"", "")
                geneDict["name"] = i
            if i.startswith("/note"):
                i = i.replace("/note=", "")
                notes = i
                if not i.endswith("\""):
                    for i in file_handle:
                        i = i.strip()
                        notes += i
                        if i.endswith("\""):
                            break
                notes = notes.replace("\"", "")
                geneDict["description"] = notes
            if i.startswith("/db_xref="):
                i = i.replace("/db_xref=", "")
                i = i.replace("\"", "")
                geneDict["id"] = i
        else:
            return geneDict,i

def parse_features(file_handle):
    features = []
    for i in file_handle:
        if i.startswith(" "):
            if i.startswith("     gene"):
                one_feature = parse_gene(file_handle, i)
                features.append(one_feature)
        else:
            return features,i

def parse_gb(file):
    file_handle = open(file, 'r')
    gbList = []
    gbDict = {}
#    raw = ""

    for i in file_handle:
#        raw += i
        if i.startswith("DEFINITION"):
            description,i = parse_def(file_handle, i)
            gbDict["description"] = description

        if i.startswith("ACCESSION"):
            id = i.replace("ACCESSION", "")
            id = id.strip()
            gbDict["id"] = id

        if i.startswith("FEATURES"):
            features,i = parse_features(file_handle)
            gbDict["features"] = features

        if i.startswith("ORIGIN"):
            origin,i = parse_origin(file_handle)
            gbDict["sequence"] = origin

        if i.startswith("//"):
            gbDict["raw"] = ""
            gbList.append(gbDict)
#            raw = ""

    #print(gbList)

    file_handle.close()
    file_handle = open(file, 'r')
    pos = 0
    raw = ""
    for i in file_handle:
        if (pos >= len(gbList)):
            break
        raw += i
        if i.startswith("//"):
            #print(pos)
            #print(len(raw))
            gbList[pos]["raw"] = raw
            raw = ""
            pos += 1
    file_handle.close()
    return gbList

def get_raw(data_object, index):
    return data_object[index]["raw"]

def get_id(data_object, index):
    #print(data_object[index])
    return data_object[index]["id"]

def get_description(data_object, index):
    return data_object[index]["description"]

def get_sequence(data_object, index):
    return data_object[index]["sequence"]

def get_fasta(dataobject, index):
    fasta = get_id(data_object,index) + get_description(data_object, index) + "\n"
    sequence = get_sequence(data_object, index)
    for i in range(0, len(sequence), 80):
        fasta += sequence[i:i+80] + "\n"
    return fasta

def get_feature(data_object, index, feature):
    return data_object[index]["features"][0][0][feature]

def add_feature(data_object, index, feature, value):
    data_object[index]["features"][0][0][feature] = value

def add_sequence_object(data_object, id, descritption, sequence, features):
    new_seq = {"id": id, "description": descritption, "sequence": sequence, "features": features}
    data_object.append(new_seq)

def get_gc_content(data_object, index):
    seq = get_sequence(data_object, index)
    count = seq.count("c") + seq.count("g")
    gc_content = count/len(seq)
    return gc_content

data_object = parse_gb("sequence.gb")

#raw = get_raw(data_object, 1)
#print(raw)

#id =get_id(data_object, 1)
#print(id)

#description = get_description(data_object, 1)
#print(description)

#sequence = get_sequence(data_object, 1)
#print(sequence)

#fasta = get_fasta(data_object, 1)
#print(fasta)

#feature = get_feature(data_object, 0, "position")
#print(feature)

#add_feature(data_object, 0, "A", 11)
#print(data_object[0])

#add_sequence_object(data_object, "TEST", "123: descritption", "agtgtgtgtgtgt", [{"name": "TEST"}])
#print(data_object[len(data_object)-1])

#gc_content = get_gc_content(data_object, 0)
#print(gc_content)
