# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:29:59 2016

@author: jose and ClemensBioinf


"""

## Aufgabe 11 & 14##
import sys

class SeqRecord:
    def __init__(self, seq, id, raw):
        self.seq = seq
        self.id = id
        self.raw = raw

    def __str__(self):
        return 'Instanz der Klasse SeqRecord.\n', self.seq.decode(), self.id.decode(), self.raw.decode()

    def __bytes__(self):
        return self.seq, self.id, self.raw

class SeqRecordFasta(SeqRecord):
    def __init__(self, seq, id, raw, description):
        super().__init__(seq, id, raw)
        self.description = description

    def __str__(self):
        return 'Instanz der Klasse SeqRecord.\n', self.seq.decode(), self.id.decode(), self.raw.decode()

    def __bytes__(self):
        return self.seq, self.id, self.raw

class SeqRecordGenbank(SeqRecordFasta):
    def __init__(self, seq, id, raw, description):
        super().__init__(seq, id, raw, description)

    def __str__(self):
        return 'Instanz der Klasse SeqRecord.\n', self.seq.decode(), self.id.decode(), self.raw.decode(),\
    self.description.decode()

    def __bytes__(self):
        return self.seq, self.id, self.raw, self.description

class Parser:
    def __init__(self, path):
        self.path = path
        self.data = []

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        for element in self.data:
            return element

    def __len__(self):
        return len(self.data)

    def fasta_parser(self):
        total_raw = bytearray(self.path)

        for sequence in total_raw.split(b'>')[1:]:
            header = sequence.partition(b' ')
            curr_seq = {}
            curr_seq['raw'] = bytes(sequence)
            curr_seq['sequence'] = b''.join(sequence.splitlines()[3:])
            curr_seq['id'] = header[0]
            curr_seq['description'] = header[2]
            self.data.append(curr_seq)
        return self.data


    def get_raw(self, db,	index):
        return db[index]["raw"].decode()

    def get_id(self, db, index):
        return db[index]["id"].decode("utf-8")

    def get_description(self, db,	index):
        return db[index]["description"].decode()

    def get_sequence(self, db, index):
        return db[index]["sequence"].decode()

    def get_fasta(self, db, index):
        header = ""
        seq = ""
        char_count = 0
        for char in db[index]["id"] + "| " + db[index]["description"]:
            char_count += 1
            if char_count % 80 == 0:
                header += "\n"
            header += char

        char_count = -1
        for char in db[index]["sequence"]:
            char_count += 1
            if char_count % 80 == 0:
                seq += "\n"
            seq += char

        return (header + seq).decode()

    def get_feature(self, db, index, feature):
        return db[index]["features"][feature].decode()

    def add_feature(self, db, index, feature, value):
        db[index]["features"][feature] = value
        return db

    def add_sequence_object(self, db, id, description, sequence, **features):
        db.append({"id":id, "description":description, "sequence":sequence, "features":features})
        return db

    def get_gc_content(self, db, index):
        seq = db[index]["sequence"].lower()
        return str(round((seq.count(b"c") + seq.count(b"g")) * 100 / len(seq),2)) + "%"

    def get_output(self, db, index, type="markdown"):
        if type == "markdown":
            output_features = ""
            for feature in db[index]["features"].keys():
                output_features += "* " + feature.upper() + ": " + db[index]["features"][feature] + "\n"
            return "#__" + db[index]["features"]["name"] + ": " + db[index]["id"].split("|")[2] + "__\n" + \
                   "##" + db[index]["description"] + "\n\n" + "__Features:__\n" + output_features + "\n---\n" + \
                   "__Sequence__:\n" + db[index]["sequence"] + "\n\n---"
        elif type == "csv": # Verbesserungswürdig. Seperator = ~
            attributes = ""
            attribute_content = ""
            for attribute in db[index].keys():
                if attribute == "features":
                    for feature in db[index]["features"].keys():
                        attributes += feature.upper() + "~"
                        attribute_content += db[index]["features"][feature] + "~"
                else:
                    attributes += attribute.upper() + "~"
                    attribute_content += db[index][attribute] +  "~"
            return attributes + "\n" + attribute_content


if __name__ == '__main__':
	print(__file__)
