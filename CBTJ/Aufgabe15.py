# Ändern Sie die Fasta Parser Funktion aus Aufgabe 6 zu
# einer Generator Funktion um, die anstatt alle Sequenzen
# in einer Liste zu speichern nur jeweils die einzelene
# Sequenz zurückgibt
# Vorteil dieser Version ist, dass wirklich immer nur eine
# Sequenz im Speicher gehalten wird und trotzdem einfach
# verwendbar bleibt. Somit kann man auch Sequenz Files
# mit mehreren GBs problemlos verarbeiten




def pars4fasta (file_path):                                         # Änderung
    file_handle = open(file_path, "r")
    list_of_dict = None                                             # Änderung


    for line in file_handle:
        if line[0] == ">":
            if list_of_dict:                                          # Änderung
                yield list_of_dict['sequence']                                   #Änderung

            id, desc = line.split(" ", maxsplit=1)
            id = id[1:]
            desc = desc.strip()

            list_of_dict =({'id': id, 'description': desc, 'sequence': "", 'raw': line}) #hängt dict an liste



        else:
            sequence = line.strip()
            list_of_dict['sequence']+=(sequence)

            list_of_dict['raw']+=(line)

    else:
        yield list_of_dict['sequence']                                      #Änderung




for i in pars4fasta("/home/claudia/ws2016/examples/sequence.fasta"):
   print (i)

#parsing = pars4fasta("/home/claudia/ws2016/examples/sequence.fasta")
#print(next(parsing))
#print(next(parsing))
#print(next(parsing))
#print(next(parsing))
#print(next(parsing))
