
import time

class SeqRecord:
    def __init__(self, id, seq, raw):
        self.id = id
        self.seq = seq
        self.raw = raw

    def getFasta(self, line_length=80):
        strings = [">{0}|{1}".format(self.id.decode(), self.desc.decode())]

        for i in range(0, len(self.seq), line_length):
            strings.append(self.seq[i:i + line_length].decode())
        return "\n".join(strings)

    def getGCcontent(self):
        sequence = self.seq.lower()
        return 100 / len(sequence) * (sequence.count(b"g") + sequence.count(b"c"))

    def getBaseContentProz(self, base):
        sequence = self.seq.lower()
        lookup = bytearray(base.lower(), encoding='utf-8')  # limiting to utf-8???

        return 100 / len(sequence) * (sequence.count(lookup))

    def getBaseContentAbs(self, base):
        sequence = self.seq.lower()
        lookup = bytearray(base.lower(), encoding='utf-8')

        return (sequence.count(lookup))

    # added acc. Aufgabe 16B => return raw as string
    def __str__(self):
        return self.raw.decode()

    # added acc. Aufgabe 16B => return raw as byte
    def __bytes__(self):
        return self.raw

    # added acc. Aufgabe 16B
    def __repr__(self):
        return "SeqRecord({0.id}, {0.seq}, {0.raw})".format(self)

class SeqRecordFasta(SeqRecord):
    def __init__(self, id, seq, raw, desc):
        super().__init__(id, seq, raw)
        self.desc = desc

    # use __fcts__ of parent, just overwrite __repr__ to add description field too
    def __repr__(self):
        return "SeqRecordFasta({0.id}, {0.seq}, {0.raw}, {0.desc})".format(self)

class SeqRecordGenbank(SeqRecordFasta):
    def __init__(self, id, seq, raw, desc, locus, version, keywords, source, organism, taxonomy, features):
        super().__init__(id, seq, raw, desc)
        self.locus = locus
        self.version = version
        self.keywords = keywords
        self.source = source
        self.organism = organism
        self.taxonomy = taxonomy
        self.features = features

    # use __fcts__ of parent, just overwrite __repr__ to add child properties too
    def __repr__(self):
        return "SeqRecordGenbank({0.id}, {0.seq}, {0.raw}, {0.desc}, {0.locus}, {0.version}, {0.keywords}," \
               " {0.source}, {0.organism}, {0.taxonomy}, {0.features})".format(self)

class Parser:
    def __init__(self):
        self.entries = []

    def parseFastaFile(self, inStream):
        db = {}
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

        self.entries.append(SeqRecordFasta(db['id'], bytes(db['seq']), bytes(db['raw']), db['desc']))

    def getRaw(self, index):
        return (self.lentries[index].raw)

    def getId(self, index):
        return (self.entries[index].id)

    def getDescription(self, index):
        return (self.entries[index].desc)

    def getSequence(self, index):
        return (self.entries[index].seq)

    # Aufgabe 17B, put here acc. github comments
    def __iter__(self):
        for item in self.entries:
            yield item

    def __getitem__(self, item):
        return self.entries[item]

    def __setitem__(self, item, value):
        self.entries[item] = value

    def __len__(self):
        return len(self.entries)

# def getGCcontent(db, index):
#
#     sequence = db[index]['sequence'].lower()
#     return 100 / len(sequence) * (sequence.count(b"g") + sequence.count(b"c"))
#
# def getBaseContentProz(db, index, base):
#
#     sequence = db[index]['sequence'].lower()
#     lookup = bytearray(base.lower(), encoding='utf-8') # limiting to utf-8???
#     return 100 / len(sequence) * (sequence.count(lookup))
#
# def getBaseContentAbs(db, index, base):
#     sequence = db[index]['sequence'].lower()
#     lookup = bytearray(base.lower(), encoding='utf-8')
#     return (sequence.count(lookup))
#
# def stopTime(func, *args, **kargs):
#     start = time.time()
#     result = func(*args, **kargs)
#
#     end = time.time()
#     print("Function {} takes {:.3} seconds".format(func.__name__, end - start))
#     return result
#
# if __name__ == "__main__":
#     print(__file__)