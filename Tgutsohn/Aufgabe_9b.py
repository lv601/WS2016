import time, io

start = time.time()

file = open("long.fasta.txt", "r")
db = []

def parser(db, file):
    for line in file:
        if line[0] == ">":
            id, description = line.split(maxsplit=1)
            db.append({'raw' : io.StringIO(line), 'id': id.lstrip(">"), 'desc': description, 'seq': io.StringIO()})
        else:
            db[-1]['seq'].write(line.rstrip())
            db[-1]['raw'].write(line)

def get_raw(db, index):
    parser(db, file)
    print(db[index]['raw'].getvalue())

def get_id(db, index):
    parser(db, file)
    print(db[index]['id'])

def get_description(db, index):
    parser(db,file)
    print(db[index]['desc'])

def get_sequence(db, index):
    parser(db, file)
    print(db[index]['seq'].getvalue())

def get_fasta(db, index):
    parser(db, file)
    str = db[index]['id']+db[index]['desc']
    strseq = db[index]['seq']
    strseq = "\n".join(strseq[i:i + 80] for i in range(0, len(strseq), 80))
    print(">" + str + strseq)

#get_raw(db, 0)
#get_id(db,0)
#get_description(db, 10)
get_sequence(db, 0)
#get_fasta(db, 0)

end = time.time()

print("{:.3} seconds".format(end - start))