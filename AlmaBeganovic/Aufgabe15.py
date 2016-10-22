def parse_fasta(file_name):
    file_handle = open (file_name,"r")
    db = None


    for line in file_handle :
        if line[0] == ">":
            if db:
               yield db


            ident, desc = line[1:].strip().split(maxsplit=1)
            db = {'id': ident,'desc': desc,'seq': ""}
        else:
           db['seq'] += line.rstrip()
    else:
        yield db

for item in parse_fasta("../AlmaBeganovic/sequence.fasta"):
    print(item)
    