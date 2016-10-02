list1 = ['RAW', 'ID', 'Description', 'Sequence']
line1 = ''

# Packen Sie das ganze noch in eine Funktion wie parse_fasta(filename)
# Sehen Sie sich das Beispiel bei ihren Kollegen oder in meinen Verzeichnis
# nochmals an
with open('/home/alma/ws2016/AlmaBeganovic/sequence.fasta') as f:
    for line in f:
        # TIPP: In dem Fall, dass nur ein Zeichen geprüft wird, können Sie auch
        # einfach den Indexoperator verwenden. Der ist schneller.

        # if line[0] == ">":
        if line.startswith(">"):
            # Achtung: hier überschreiben sie line mit der split ergebnisliste,
            # die Sie dann noch in eine leere Liste packen
            line = [line.rstrip().split('|')]
            id = line[0][0] + '|' + line[0][1]
            description = line[0][4]
            # TIPP: verwenden Sie eine Liste mit Dictionaries, So überschreiben
            # Sie sich alles bei der nächsten Sequenz
            # [{seq1...}, {seq2...}, {seq3...}, ...]
            list1[1] = "ID:", id
            list1[2] = "Description:", description
            print (list1)
        else:
            line1 = line + line1
            list1[3] = "Sequence:", line1
