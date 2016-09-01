#
# Structure: [ {'raw': <raw fasta sequence>, 'id': <header>, 'reference': <reference>, 'description': <description>,
#               'sequence': <fasta-sequence>}, <next entry>, <next entry>]

def parse_fasta(file):
    file_handle = open(file,'r')
    fastaList = []
    fastaDict = {}
    for line in file_handle:
        if line.startswith('>'):
            #fasta_header = line
            fastaDict['id'] = line.split(" ")[0]
            fastaDict["description"] = (" ".join(line.split(" ")[1:])).strip('\n')
            fastaDict["sequence"] = ""
            fastaDict['raw'] = line
            fastaList.append(fastaDict)
        else:
            fastaList[len(fastaList)-1]['sequence'] += line.strip('\n')
            fastaList[len(fastaList)-1]['raw'] += line
    return fastaList

def get_raw(db, index):
    return db[index]['raw']

def get_id(db, index):
    return db[index]['id']

def get_description(db, index):
    return db[index]['description']

def get_sequence(db, index):
    return db[index]['sequence']

def get_fasta(db, index):
    fasta = get_id(db, index) + get_description(db, index) + '\n'
    fasta += insert_linebreak(get_sequence(db, index),80)
    return fasta

def insert_linebreak(string, length):
    lines = ''
    for i in range(0, len(string), length):
        lines += string[i:i+length] + '\n'
    return lines

def get_feature (db, index, feature):
    if feature in db[index]:
        return db[index][feature]
    else:
        return "No such key available"

def add_feature(db, index, feature, value):
    db[index][feature]=value

def get_gc_content(db, index):
    sequence = db[index]['sequence']
    return (sequence.count('C') + sequence.count('G'))/len(sequence)

db = parse_fasta('../examples/sequence.fasta')
#print(get_raw(db,1))
#print(get_id(db,1))
#print(get_description(db,1))
#print(get_sequence(db,1))
#print(get_fasta(db,1))
#print(get_feature(db, 1, 'id'))

print(add_feature(db, 1, 'organism', 'test'))
print(get_feature(db, 1, 'organism'))
print(get_gc_content(db,1))