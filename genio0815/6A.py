

def parseFastaFile(file):

    file_handler = open(file, 'r')
    seq_list = []

    for line in file_handler:

        if line.startswith('>'):
            seq_dict = dict()
            seq_dict['id'] = line.split()[0][1:]
            seq_dict['description'] = line.split(maxsplit=1)[1].strip()  # .rstrip('\n')
            seq_dict['sequence'] = ""
            seq_dict['raw'] = line.rstrip('\n')
            seq_list.append(seq_dict)
        else:
            str1 = line.strip('\n')
            seq_list[len(seq_list)-1]['sequence'] += str1
            seq_list[len(seq_list)-1]['raw'] += str1

    return seq_list

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
