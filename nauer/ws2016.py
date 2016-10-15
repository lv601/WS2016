#! /usr/bin/env python3

""" Aufgaben 11
Erstellen sie in ihrem Projektordner eine Datei mit dem Namen ws2016.py und eine weitere mit dem Namen fasta_parser.py.
Kopieren Sie den Code der schnellsten fasta_parser Implementierung nach ws2016.py. Formen Sie die Funktiondefinition so
um, dass sie einen Stream anstelle eines Filenamens übergeben. Importieren Sie in fasta_parser.py das Modul ws2016 und
rufen Sie die fasta_parser Funktion auf. Erstellen Sie fasta_parser.py so, dass es den Filenamen aus der Kommandozeile
mit sys.argv liest
"""

import time
import sys

class Feature:
    def __init__(self, name, start, end, **kargs):
        self.fields = dict(kargs)
        self.name = name
        self.start = start
        self.end = end

        self.max_lengh = max(map(len,list(self.fields.keys())))

    def __str__(self):
        string = "{0.name} {0.start}..{0.end}\n".format(self)

        for key in self.fields:
            string += ("  {:<" + str(self.max_lengh) + "} = {}\n").format(key, self.fields[key].decode())
        return string

class SeqRecord:
    def __init__(self, id , seq, raw):
        self.id = id
        self.seq = seq
        self.raw = raw

    def __str__(self):
        return self.raw.decode()

    def get_raw(self):
        """
        Return original text data
        :param db:
        :param index:
        :return: str
        """
        return self.raw.decode()

    def get_fasta(self, line_length=80):
        """
        Return sequence in fasta format
        :param db:
        :param index:
        :return: str
        """
        strings = [">{0}|{1}".format(self.id.decode(), self.desc.decode())]

        for i in range(0, len(self.seq), line_length):
            strings.append(self.seq[i:i + line_length].decode())
        return "\n".join(strings)

    def get_gc_content(self):
        """
        Returns the % GC content
        :param db:
        :param index:
        :return: float
        """
        seq = self.seq.lower()
        return 100 / len(seq) * (seq.count(b"g") + seq.count(b"c"))

class SeqRecordFasta(SeqRecord):
    def __init__(self, id, seq, raw, desc):
        super().__init__(id, seq, raw)
        self.desc = desc


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

class Parser:
    def __init__(self):
        self._records = []

    def __iter__(self):
        for item in self._records:
            yield item

    def __getitem__(self, item):
        return self._records[item]

    def __setitem__(self, item, value):
        self._records[item] = value

    def parse_fasta(self, stream):
        # Test if stream from type binary
        if isinstance(stream.read(0), (bytes, bytearray)):
            db = {}
            for line in stream:
                if line[0] == 62:  # ord(">") bytes are stored as numbers
                    if db:
                        self._records.append(SeqRecordFasta(**db))
                        db = {}

                    # New fasta sequence starts - parse header
                    ident, sep, desc = line[1:].strip().partition(b" ")

                    db = {'id': ident,
                          'desc': desc,
                          'seq': bytearray(),  # Switch to bytearray
                          'raw': bytearray(line)}  # Switch to bytearray
                else:
                    # Sequence line
                    db['seq'] += (line.rstrip())
                    db['raw'] += (line)
        else:
            print("Stream must be opened as binary", file=sys.stderr)
            # Exit script with -1. Signals an error to the operationg system
            exit(-1)

    def parse_genbank(self, stream):
        # Define subparser to parse main fields
        subparser = {b'LOCUS': self._LOCUS,
                     b'DEFINITION': self._DEFINITION,
                     b'ACCESSION': self._ACCESSION,
                     b'VERSION': self._VERSION,
                     b'KEYWORDS': self._KEYWORDS,
                     b'SOURCE': self._SOURCE,
                     b'FEATURES': self._FEATURES,
                     b'ORIGIN': self._ORIGIN}

        # Test if stream from type binary
        if isinstance(stream.read(0), (bytes, bytearray)):
            raw = bytearray()
            db = {}
            result = {}
            for line in stream:
                raw += line

                # Remove empty lines
                if len(line.strip()) == 0:
                    continue

                # End of entry
                if line[:2] == b"//":
                    for key in db:
                        if key in subparser:
                            subparser[key](db, result)
                        else:
                            pass # save in others

                    self._records.append(SeqRecordGenbank(**result, raw=raw))
                    # Reset variables for next sequence
                    raw = bytearray()
                    db = {}
                    continue

                # Search for main fields like LOCUS or DEFINITION
                if not line.rstrip().startswith(b" "):  # ord(" ") bytes are stored as numbers
                    key = line.partition(b" ")[0]
                    db[key] = bytearray(line)
                else:
                    # Sequence line
                    db[key] += line
        else:
            print("Stream must be opened as binary", file=sys.stderr)
            # Exit script with -1. Signals an error to the operationg system
            exit(-1)

    def _LOCUS(self, db, result):
        locus = db[b'LOCUS'].split()
        result['locus'] = bytes(b" ".join(locus[1:]))

    def _DEFINITION(self, db, result):
        result['desc'] = self._multiline_text(db, b'DEFINITION')

    def _ACCESSION(self, db, result):
        acc = db[b'ACCESSION'].split()
        result['id'] = bytes(acc[1])

    def _VERSION(self, db, result):
        result['version'] = self._multiline_text(db, b'VERSION')

    def _KEYWORDS(self, db, result):
        result['keywords'] = self._multiline_list(db, b"KEYWORDS", b";")
        # Remove ending .
        result['keywords'][-1] = result['keywords'][-1][:-1]

    def _SOURCE(self, db, result):
        source = db[b'SOURCE'].splitlines()
        result['source'] = bytes(source[0].strip().partition(b" ")[2].strip())
        result['organism'] = bytes(source[1].strip().partition(b" ")[2].strip())
        result['taxonomy'] = []

        for tax in source[2:]:
            for t in tax.split(b";"):
                result['taxonomy'].append(bytes(t.strip()))

        # Remove ending .
        result['taxonomy'][-1] = result['taxonomy'][-1][:-1]

    def _FEATURES(self, db, result):
        features = db[b'FEATURES'].splitlines()

        feature_list = []
        feature = {}
        sub_feat = None
        for l in features[1:]:
            if l[6] != 32:
                if feature:
                    feature_list.append(Feature(name=feat_name, **feature[feat_name]))
                    feature = {}

                part = l.strip().partition(b" ")
                feat_name = part[0].decode()
                pos = part[2].strip().partition(b"..")
                feature[feat_name] = {'start':int(pos[0]), 'end':int(pos[2])}
            elif l.strip().startswith(b"/"):
                part2 = l.strip().partition(b"=")
                sub_feat = part2[0][1:].decode()
                feature[feat_name][sub_feat] = bytes(part2[2].strip(b"\""))
            else:
                feature[feat_name][sub_feat] += bytes(l.strip().strip(b"\""))

        if feature:
            feature_list.append(Feature(name=feat_name, **feature[feat_name]))

        result['features'] = feature_list

    def _ORIGIN(self, db, result):
        origin = db[b'ORIGIN'].splitlines()

        res = bytearray()

        for l in origin[1:]:
            res += b"".join(l.split()[1:])

        result['seq'] = bytes(res)

    def _multiline_text(self, db, key):
        content = db[key].partition(b" ")[2].splitlines()
        res = bytearray(content[0].strip())

        for l in content[1:]:
            res += l.strip()

        return bytes(res)

    def _multiline_list(self, db, key, sep):
        content = db[key].partition(b" ")[2].split(sep)
        res = []

        for l in content:
            res.append(bytes(l.strip()))

        return res

    def add_record(self, record):
        """
        Add a new record to Parser
        :param record:
        :return:
        """
        self._records.append(record)

        # returns the index of that record
        return len(self._records) - 1



    def add_sequence_object(self, id, description, sequence, *features):
        """
        Add a new sequence to data dictionary
        :param db:
        :param id:
        :param description:
        :param sequence:
        :param features: Any kind of feature not mentioned in the main features
        :return: None
        """
        self._records.append({'id': bytes(id), 'description': bytes(description), 'sequence': bytes(sequence), 'features': features})



class Misc:
    @staticmethod
    # Stop time of function calls
    def stop_time(func, *args, **kargs):
        start = time.time()

        result = func(*args, **kargs)

        end = time.time()
        print("Function {} takes {:.3} seconds".format(func.__name__, end - start))
        return result


# Test if library have been imported or run directly
if __name__ == "__main__":
    # Run test code
    print(__file__)
    print(__name__)

    # rec = SeqRecordGenbank("id1112", "ATTGCCGTT")
    parser = Parser()

    with open("../examples/sequence.fasta", "rb") as f:
        parser.parse_fasta(f)

        print(parser._records[1].id)
        print(parser[2].id)
        print(parser._records[3].id)
        print(parser._records[1])

        print(parser[1].get_fasta())

        print(parser[1].get_gc_content())

    with open("../examples/sequence.gb", "rb") as f:
        parser.parse_genbank(f)
        print(parser._records[10].id)
        print(parser._records[10].seq)
        print(parser._records[10].desc)
        print(parser._records[10].locus)
        print(parser._records[10].version)
        print(parser._records[10].keywords)
        print(parser._records[10].source)
        print(parser._records[10].organism)
        print(parser._records[10].taxonomy)
        print(parser._records[10].raw)
        print(parser._records[10])
        print(parser._records[10].features[0])
        print(parser._records[10].features[1])
        print(parser._records[10].features[2])
        print(parser._records[10].features[0].name)

        for item in parser:
            print(item.id)




















