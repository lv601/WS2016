# Ueberarbeitete Aufgabe 6a:

def parse_fasta(file):
    file_handle = open(file, 'r')
    fastadict = None
    for line in file_handle:
        if line[0] == ">":
            if fastaList:
                yield fastadict
                fastadict = None

            id, description = line[1:].strip().split(maxsplit=1)
            fastadict = {"id":id, "description": description, "seq": "", "raw":line}

        else:
            fastadict['seq'] += line.rstrip()
            fastadict['raw'] += line
    else:
        yield fastadict

print(parse_fasta("sequence.fasta"))

