def fasta_parser2(filename):
    """fasta parser, reads fasta file and introduces content into list"""
    file_handle = open(filename, "rb")

    for index, line in enumerate(file_handle):

        if line[0] == 62:

            header, desc = line.split(maxsplit=1)
            header = header[1:]
            desc = desc.strip()
            if index == 0:

                db = [{"id": header, "desc": desc, "sequence": bytearray(), "raw": line}]
            else:
                db.append({"id":header, "desc":desc, "raw":line, "sequence":bytearray()})
        else:
            line = line.strip()
            db[-1]['sequence'] += line
            db[-1]['raw'] += line
    return(db)


#Zeitmessung

import time

start = time.time()
fasta_parser("../examples/long.fasta")
end = time.time()
print("Dauer des Parsens mit Strings: {:.3} Sekunden".format(end-start))

start = time.time()
fasta_parser2("../examples/long.fasta")
end = time.time()
print("Dauer des Parsens mit Bytearray: {:.3} Sekunden".format(end-start))