import time, io

start = time.time()

file = open("long.fasta.txt", "rb")
db = []

def parser(db, file):
    for line in file:
        if line[0] == 62:
            id, description = line.split(maxsplit=1)
            db.append({'raw' : io.BytesIO(line), 'id': id.lstrip(), 'desc': description, 'seq': io.BytesIO()})
        else:
            db[-1]['seq'].write(line.rstrip())
            db[-1]['raw'].write(line)

def get_raw(db, index):
    parser(db, file)
    print(db[index]['raw'].getvalue().decode())

def get_id(db, index):
    parser(db, file)
    print(db[index]['id'].decode())

def get_description(db, index):
    parser(db,file)
    print(db[index]['desc'].decode())

def get_sequence(db, index):
    parser(db, file)
    print(db[index]['seq'].getvalue().decode())

# def get_fasta(db, index):
#     parser(db, file)
#     str = db[index]['id']+db[index]['desc']
#     strseq = db[index]['seq']
#     strseq = "\n".join(strseq[i:i + 80] for i in range(0, len(strseq), 80))
#     print(">" + str + strseq)

#get_raw(db, 2)
get_id(db,0)
get_description(db, 0)
#get_sequence(db, 0)
#get_fasta(db, 3)
print("\n")



end = time.time()

print("{:.3} seconds".format(end - start))