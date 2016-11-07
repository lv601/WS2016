# Ueberarbeitete Aufgabe 6a:

def parse_fasta(file):
    file_handle = open(file, 'r')
    fastaDict = None

    for line in file_handle:
        if line[0] == ">":
            if fastaDict:
                yield fastaDict
            id, description = line[1:].strip().split(maxsplit=1)
            fastaDict = {"id": id, "description": description, "sequence": ""}
        else:
            fastaDict["sequence"] += line.rstrip()
    else:
        yield fastaDict
    #
    #         parts = line[1:].partition(" ")
    #         fastaDict["id"] = parts[0]
    #         fastaDict["description"] = parts[2]
    #         fastaDict["raw"] = line
    #         fastaDict["sequence"] = ""
    #         fastaList.append(fastaDict)
    #     else:
    #         # \n am Ende jeder Zeile entfernen
    #         sequence = line[:-1]
    #         #print(sequence)
    #         fastaList[-1]["sequence"] += sequence
    #         fastaList[-1]["raw"] += line
    # return(fastaList)

print("erstes: ")
print(parse_fasta("sequence.fasta"))

print("zweites:")
print(list(parse_fasta("sequence.fasta")))

print("drittes")
for item in parse_fasta("sequence.fasta"):
    print(item)

print("viertes:")
print(next(parse_fasta("sequence.fasta")))