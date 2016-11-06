class SeqRecord:
    def __init__(self, id, seq, raw):
        self.id = id
        self.seq = seq
        self.raw =raw

class SeqRecordFasta(SeqRecord):
    def __init__(self, id, seq, raw, decription):
        super()._init_(id, seq, raw)
        self.desc = description

class SeqRecordGenbank(SeqRecordFasta):
            def __init__(self, id, seq, raw, decription):
                super()._init_(id, seq, raw, description)
                pass
class Parser:
    def _init_(self):
         self.record =[]

    def add_record(self. record):
         self.record.append(record)

         return len(sef.record) -1


    def parse(self, stream, type="fasta"):
        if instance(stream.)
