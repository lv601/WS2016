import sys, io

class SeqRecord:
    def __init__(self, id, seq, raw):
        self.id = id
        self.seq = seq
        self.raw =raw

    def __str__(self):
        return self.raw.decode()

    def __bytes__(self):
        return self.raw

    def __repr__(self):
        return "SeqRecord({0.id}, {0.seq}, {0.raw})".format(self)


class SeqRecordFasta(SeqRecord):
    def __init__(self, id, seq, raw, description):
        super().__init__(id, seq, raw)
        self.desc = description

    def __repr__(self):
        return "SeqRecordFasta({0.id}, {0.seq}, {0.raw}, {0.description})".format(self)


class Parser:
    def __init__(self):
         self.records = []

    def __iter__(self):
        for item in self._records:
            yield item

    def __getitem__(self, item):
        return self._records[item]

    def __setitem__(self, item, value):
        self._records[item] = value

    def __len__(self):
        return len(self._records)

    def add_record(self, record):
         self.record.append(record)
         return len(self.record) -1

    def parse(self, stream, type="fasta"):
        if isinstance(stream.read(0), bytes):
            db = []
            for line in stream:
                if line[0] == 62:  #
                    header, desc = line.split(maxsplit=1)
                    header = header[1:]
                    desc = desc.strip()
                    db.append({"id": header, "desc": desc, "raw": io.BytesIO(line), "sequence": io.BytesIO()})
                else:
                    line = line.strip()
                    db[-1]['sequence'].write(line)
                    db[-1]['raw'].write(line)
            return (db)
        else:
            print("Der Stream muss binaer sein.", file=sys.stderr)
            exit(-1)
