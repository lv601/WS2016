
def parseFastaFile(inStream):
    db = []
    for line in inStream:
        if line[0] == 62:  # bin token for ">"
            ident, desc = line[1:].strip().split(maxsplit=1)
            db.append({'id': ident,
                       'description': desc,
                       'sequence': bytearray(),
                       'raw': bytearray(line)})
        else:
            db[-1]['sequence'] += (line.rstrip())
            db[-1]['raw'] += (line)

    return db

if __name__ == "__main__":
    print(__file__)