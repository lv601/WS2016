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
            fastaList[len(fastaList)-1]["sequence"] += sequence # auch [:-1] schneller u python spezifisch
            fastaList[len(fastaList)-1]["raw"] += i
    return(fastaList)

#result = parse_fasta("sequence.fasta")
#for i in result:
#    print(i)
print(parse_fasta("sequence.fasta"))
