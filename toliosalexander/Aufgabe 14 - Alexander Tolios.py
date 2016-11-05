### Aufgabe 14 - Alexander Tolios - last modified 29.10.2016 

import sys
import time

class SeqRecord:
    def __init__(self, id, seq, raw):
        self.id = id
        self.seq = seq
        self.raw = raw

class SeqRecordFasta(SeqRecord):
    def __init__(self, id, seq, raw, description):
        super().__init__(id, seq, raw)
        self.desc = description

class SeqRecordGenbank(SeqRecordFasta):
    def __init__(self, id, seq, raw, description):
        super().__init__(id, seq, raw, description)
        pass

class Parser:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.append(record)
		return lens(self.record)-1 ######## CAVE: funktioniert nicht! TabError: inconsistent use of tabs and spaces in indentation

    def fasta_parsa_bIO(self, stream, type="fasta-file"):
		if isinstance(stream.read(0),(bytes, bytearray)):
              db={}
              for line in stream:
                  if line[0] == 62:
                      if db:
                          self._records.append()


