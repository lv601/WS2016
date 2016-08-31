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

    for entry in total_raw.split("//"):
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
            if curr_attribute == "LOCUS":
                curr_entry["id"] = line.split(" ")[7]
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

#fasta_parser("WS2016/examples/sequence.fasta")

#genbank_parser("WS2016/examples/sequence.gb")
