file_handle = open("/home/julie/Desktop/FH/EPROG/examples/sequence.fasta", "r")

db =[{}]

for line in file_handle:
    if line.startswith(">"): #wenn das hier TRUE ist, dann wird ein neues Objekt erstellt und die anschließenden Sachen werden auf die weiteren Indices weiter gegeben
        description, id = line[1:].split(maxsplit=1) #aus beiden Teilen wird eine Variable erstellt; es wird genau einmal gesplittet
        #print(description)
        #print(id)
        db = {"id":id, "description":description}
        #print(db)
    else:
        raw = line
        #print(raw) #dings.strip()
        sequence = line.rstrip()
        db["sequence"] = sequence

print(db)