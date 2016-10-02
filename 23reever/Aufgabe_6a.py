# Ueberarbeitete Aufgabe 6a:

def parse_fasta(file):
    file_handle = open(file, 'r')
    fastaList = []
    for line in file_handle:
        fastaDict = {}
        #Kopfzeile erkennen
        if line[0] == ">":
            parts = line[1:].partition(" ")
            fastaDict["id"] = parts[0]
            fastaDict["description"] = parts[2]
            fastaDict["raw"] = line
            fastaDict["sequence"] = ""
            fastaList.append(fastaDict)
        else:
            # \n am Ende jeder Zeile entfernen
            sequence = line[:-1]
            #print(sequence)
            fastaList[-1]["sequence"] += sequence
            fastaList[-1]["raw"] += line
    return(fastaList)

print(parse_fasta("sequence.fasta"))

# Fasta Seq öffnen, einlesen in Reihe von Dicts schreiben
# (raw=originalinhalt,id=bis erste Leerzeichen ohne ">", description=2.Teil Kopfzeile (alles nach Leerzeichen),
# sequence=rest ohne whitespace)

def parse_fasta(file):
    file_handle = open(file, 'r')
    fastaList = []
    #Ausgebessert in VO -> würde sich selbst überschreiben
    #fastaDict = {}
    for i in file_handle:
        fastaDict = {} # dict besser hier anlegen, dann funktionierts
        #Kopfzeile erkennen
        if i.startswith(">"):
            #print(fastaDict)
            id = i.split(" ")[0]
            id = id.strip(">")
            fastaDict["id"] = id
            #print(fastaDict)
            description = i[len(id) + 2:len(i)]
            #print(description)
            fastaDict["description"] = description
            #print(fastaDict)
            fastaDict["raw"] = i
            fastaDict["sequence"] = ""
            #print(fastaDict)
            fastaList.append(fastaDict)
            #print(fastaList)
        else:
            sequence = ''.join(i.split())
            #print(sequence)
            fastaList[len(fastaList)-1]["sequence"] += sequence # auch [-1] schneller u python spezifisch
            fastaList[len(fastaList)-1]["raw"] += i
    return(fastaList)

#result = parse_fasta("sequence.fasta")
#for i in result:
#    print(i)
print(parse_fasta("sequence.fasta"))
