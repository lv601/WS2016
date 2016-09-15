# Fasta Seq öffnen, einlesen in Reihe von Dicts schreiben
# (raw=originalinhalt,id=bis erste Leerzeichen ohne ">", description=2.Teil Kopfzeile (alles nach Leerzeichen),
# sequence=rest ohne whitespace)

def parse_fasta(file):
    file_handle = open(file, 'r')
    fastaList = []
    #Ausgebessert in VO -> würde sich selbst überschreiben
    #fastaDict = {}
    # TIPP: Verwenden Sie sprechende Namen für ihre Variablen. In diesem Falle
    # wäre line oder zeile angebracht. i, j, k verwenden sie eher in Kombination
    # mit range(), wenn Sie als index verwenden
    for i in file_handle:
        fastaDict = {} # dict besser hier anlegen, dann funktionierts
        #Kopfzeile erkennen
        # TIPP: Wenn Sie wie hier nur auf ein Zeichen prüfen, können Sie auch
        # den Indexoperator benutzen. Der ist schneller.
        # if zeile[0] == ">":
        if i.startswith(">"):
            #print(fastaDict)

            # TIPP Anstatt ">" zu strippen, können Sie es einfach bevor der
            # split Aktion einfach weg lassen, zumal es sich sowieso nur um das
            # erste Zeichen handelt.
            # id = zeile[1:].split(" ")[0]
            id = i.split(" ")[0]
            id = id.strip(">")
            fastaDict["id"] = id
            #print(fastaDict)

            # TIPP Das brauchen Sie nicht. Sie haben den gesuchten String
            # bereits in der split Liste. Sie können die Liste explizit in einer
            # Variable speichern und darauf indexieren oder entpacken die Liste
            # einfach direkt.
            #
            # fastaDict["id"], fastaDict["description"] = zeile[1:].split(" ")
            #
            # Noch besser würde sich hier die string Methode .partition()
            # eignen, da Sie sicher immer 3 Strings zurück bekommen,
            # ([part1, sep, part2]) falls im Header mal keine Desription
            # vorkommt. Bei split würde das sonst einen Error werfen, wenn Sie
            # auf das 2 Segment zugreifen würden.
            #
            # partiotions = zeile[1:].partition(" ")
            # fastaDict["id"] = partiotions[0]
            # fastaDict["description"] = partiotions[2]

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
            # Macht keinen Sinn. i besteht nur aus einer Zeile
            sequence = ''.join(i.split())
            #print(sequence)
            fastaList[len(fastaList)-1]["sequence"] += sequence # auch [:-1] schneller u python spezifisch
            fastaList[len(fastaList)-1]["raw"] += i
    return(fastaList)

#result = parse_fasta("sequence.fasta")
#for i in result:
#    print(i)
print(parse_fasta("sequence.fasta"))
