#####Aufgabe_11###

from pprint import pprint

def parse_fasta_bytearray(file, db):
    file_handle = open('sequence.fasta','rb')

    for line in file_handle:
        datadict = {}
        if line[0] == 62:
           ID, Descr = line[1:].strip().split(maxsplit = 1)
           datadict['ID'] = ID
           datadict['Description'] = Descr
           datadict['raw'] = bytearray(line) 
           datadict['Sequence'] = bytearray()
           db.append(datadict)
           
        else:
            db[-1]['Sequence'] += (line.rstrip())
            db[-1]['raw'] += (line[:-1])
    return(db)
db = []

def get_gc_content(db, index):
    seq = db[index]['Sequence']
    count = 0
    for ind, char in enumerate(seq):
        if (char == "A") or (char == "T"):
            continue
        else:
            count +=1
    content = count / (ind+1)
    content *= 100
    return content


if __name__ == '__main__':
    print(__file__)
