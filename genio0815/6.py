
# db [{seq1}, {seq2}, {seq3}, ...] Sequence of dictionaries...acc requirements

import re

def parseFastaFile(db,file):

    """
    Parse a multi sequence fasta file and map it to a dictionary...acc requirements
    :param db:
    :param file:
    :return: None
    """

    file_handler = open(file, 'r')

    for line in file_handler:
        if line[0] == ">":
            fastaId = line.split()[0][1:]
            desc = line.split(maxsplit=1)[1].strip()
            db.append({'id': fastaId, 'description': desc, 'sequence': "", 'raw': line})
        else:
            db[len(seq_list)-1]['sequence'] += line.rstrip()
            db[len(seq_list)-1]['raw'] += line

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

#########

def parseGb(db, file):
    """
    Parse a multi sequence genbank file and map it to a dictionary
    The main loop runs first. It seperates the genbank sequences. Then the secondary loop seperates different fields in
    the genbank sequence
    :param db:
    :param file_name:
    :return: None
    """
    rawData = []
    raw = ""

    with open(file,'r') as inFile:
        for line in inFile:
            if line.startswith("//"):
                raw += 'DONE'  # end token for regex
                rawData.append(raw)
                raw = line
            else:
                raw += line

    # (dbId, start token, end token)
    gbStructure = [('id', 'ACCESSION', 'VERSION'), ('description', 'DEFINITION', 'ACCESSION'),
                 ('sequence', 'ORIGIN', 'DONE'), ('features', 'FEATURES', 'ORIGIN'),
                 ('organism', 'ORGANISM', 'COMMENT')]

    for i in range(len(rawData)):
        for dbId, fromStr, toStr in gbStructure:
            #db[-1][dbId] = re.search(fromStr + r'(.*?)' + toStr, rawData[i],re.DOTALL).group(1)
            aux = re.search(fromStr + r'(.*?)' + toStr, rawData[i], re.DOTALL).group(1)
            print("for {} found {}".format(dbId, aux))

    return None

test = dict()
testfile = "../examples/sequence.gb"
parseGb(test, testfile)




