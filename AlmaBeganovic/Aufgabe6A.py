list1 = ['RAW', 'ID', 'Description', 'Sequence']
line1 = ''
with open('/home/alma/ws2016/AlmaBeganovic/sequence.fasta') as f:
    for line in f:
        if line.startswith(">"):
            line = [line.rstrip().split('|')]
            id = line[0][0] + '|' + line[0][1]
            description = line[0][4]
            list1[1] = "ID:", id
            list1[2] = "Description:", description
            print (list1)
        else:
            line1 = line + line1
            list1[3] = "Sequence:", line1