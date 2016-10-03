
# db [{seq1}, {seq2}, {seq3}, ...] Sequence of dictionaries...acc requirements

def parseFastaFile(db,file):

    """
    Parse a multi sequence fasta file and map it to a dictionary
    :param db:
    :param file_name:
    :return: None
    """

    file_handler = open(file, 'r')

    for line in file_handler:
        if zeile[0] == ">":
            db['id'] = line.split()[0][1:]
            db['description'] = line.split(maxsplit=1)[1].strip()  # .rstrip('\n')
            db['sequence'] = ""
            db['raw'] = line.rstrip('\n')
            db.append(seq_dict)
        else:
            str1 = line.strip('\n')
            db[len(seq_list)-1]['sequence'] += str1
            db[len(seq_list)-1]['raw'] += str1

result = parseFastaFile('../examples/sequence.fasta')

for i in range(0, len(result)):
    print(result[i]['description'])

def get_raw(db,index):
    return db[index]['raw']

def get_id(db,index):
    return db[index]['id']

def get_description(db, index):
    return db[index]['description']

def get_sequence(db, index):
    return db[index]['sequence']

def get_fasta(db,index):
    fasta = db[index]['id'] + " " + db[index]['description'] + '\n'

    seq = None
    step = 80
    instr = db[index]['sequence']

    for i in range(0, len(instr), step):
        seq += instr[i:i+step] + '\n'

    fasta += seq
    return fasta

def get_feature(db, index, feature):







#def parseDB(db, inFile):
