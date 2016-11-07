#!/usr/bin/python3.5
import io

class SeqRecord():
    def get_raw(self, index):
        return self.data_object[index]["raw"]

    def get_id(self, index):
        #print(self.data_object[index])
        return self.data_object[index]["id"]

    def get_description(self, index):
        return self.data_object[index]["description"]

    def get_sequence(self, index):
        return self.data_object[index]["sequence"]

    def get_fasta(self, index):
        fasta = self.get_id(index) + self.get_description(index) + b"\n"
        sequence = self.get_sequence(index)
        for i in range(0, len(sequence), 80):
            fasta += sequence[i:i+80] + b"\n"
        return fasta

    def get_gc_content(self, index):
        seq = self.get_sequence(index)
        count = seq.count(b"C") + seq.count(b"c") + seq.count(b"g") + seq.count(b"G")
        gc_content = count/len(seq)
        return gc_content

class SeqRecordFasta(SeqRecord):
    def __repr__(self):
            return "SeqRecordFasta"

    def __str__(self):
        raw = ""
        length = len(self.data_object)
        for item in range(length):
            raw += str(self.get_raw(item))
        return raw

    def __bytes__(self):
        raw = b""
        length = len(self.data_object)
        for item in range(length):
            raw += self.get_raw(item)
        return raw

    def parse(self, filename):
        file_handle = open(filename, "rb")
        parser = Parser()
        self.data_object = parser.parse_fasta_bytearray(file_handle)

    def __getitem__(self, item):
        return self.data_object[item]

    def __iter__(self):
        for item in self.data_object:
            yield item

    def __len__(self):
        return len(self.data_object)


class SeqRecordGenbank(SeqRecord):
    def parse(self, filename):
        parser = Parser()
        self.data_object = parser.parse_gb(filename)

    def __repr__(self):
        return "SeqRecordGenbank"

    def __str__(self):
        raw = ""
        length = len(self.data_object)
        for item in range(length):
            raw += str(self.get_raw(item))
        return raw

    def __bytes__(self):
        raw = b""
        length = len(self.data_object)
        for item in range(length):
            raw += self.get_raw(item)
        return raw

    def __getitem__(self, item):
        return self.data_object[item]

    def __iter__(self):
        for item in self.data_object:
            yield item

    def __len__(self):
        return len(self.data_object)

class Parser():
    def parse_def(self, file_hanlde, firstline):
        definition = firstline.replace(b"DEFINITION", b"")
        definition = definition.strip()

        for i in file_hanlde:
            if i.startswith(b" "):
                definition += i.strip()
            else:
                return definition, i

    def parse_origin(self, file_handle):
        origin = b""
        for i in file_handle:
            if i.startswith(b" "):
                i = i.strip()
                first = 1
                for j in i.split(b" "):
                    if not first:
                        origin += j
                    else:
                        first = 0
            else:
                return origin, i

    def parse_gene(self, file_handle, firstline):
        geneDict = {}
        position = firstline.replace(b"     gene", b"")
        position = position.strip()
        geneDict["position"] = position
        # print(position)
        for i in file_handle:
            if i.startswith(b"      "):
                i = i.strip()
                if i.startswith(b"/gene"):
                    i = i.replace(b"/gene=", b"")
                    i = i.replace(b"\"", b"")
                    geneDict["name"] = i
                if i.startswith(b"/note"):
                    i = i.replace(b"/note=", b"")
                    notes = i
                    if not i.endswith(b"\""):
                        for i in file_handle:
                            i = i.strip()
                            notes += i
                            if i.endswith(b"\""):
                                break
                    notes = notes.replace(b"\"", b"")
                    geneDict["description"] = notes
                if i.startswith(b"/db_xref="):
                    i = i.replace(b"/db_xref=", b"")
                    i = i.replace(b"\"", b"")
                    geneDict["id"] = i
            else:
                return geneDict, i

    def parse_features(self, file_handle):
        features = []
        for i in file_handle:
            if i.startswith(b" "):
                if i.startswith(b"     gene"):
                    one_feature = self.parse_gene(file_handle, i)
                    features.append(one_feature)
            else:
                return features, i

    def parse_gb(self, file):
        file_handle = open(file, "rb")
        gbList = []
        gbDict = {}
        #    raw = ""

        for i in file_handle:
            #        raw += i
            if i.startswith(b"DEFINITION"):
                description, i = self.parse_def(file_handle, i)
                gbDict["description"] = description

            if i.startswith(b"ACCESSION"):
                id = i.replace(b"ACCESSION", b"")
                id = id.strip()
                gbDict["id"] = id

            if i.startswith(b"FEATURES"):
                features, i = self.parse_features(file_handle)
                gbDict["features"] = features

            if i.startswith(b"ORIGIN"):
                origin, i = self.parse_origin(file_handle)
                gbDict["sequence"] = origin

            if i.startswith(b"//"):
                gbDict["raw"] = b""
                gbList.append(gbDict)
                #            raw = ""

        # print(gbList)

        file_handle.close()
        file_handle = open(file, 'rb')
        pos = 0
        raw = b""
        for i in file_handle:
            if (pos >= len(gbList)):
                break
            raw += i
            if i.startswith(b"//"):
                # print(pos)
                # print(len(raw))
                gbList[pos]["raw"] = raw
                raw = b""
                pos += 1
        file_handle.close()
        return gbList

    def parse_fasta_bytearray(self, file_handle):
        fastaList = []
        for line in file_handle:
            fastaDict = {}
            #Kopfzeile erkennen
            if line[0] == ord(">"):
                parts = line[1:].strip().split(maxsplit=1)
                #print(parts)
                fastaDict["id"] = parts[0]
                fastaDict["description"] = parts[1]
                fastaDict["raw"] = line
                fastaDict["sequence"] = bytearray()
                fastaList.append(fastaDict)
                #print(fastaList)
            else:
                #print(type(line))
                fastaList[-1]["sequence"] += bytearray(line[:-1])
                fastaList[-1]["raw"] += line
        return fastaList

# Testcode
if __name__ == "__main__":
    seq = SeqRecordFasta()
    seq.parse("sequence.fasta")
    #
    # print("Fasta")
    # print(seq.get_gc_content(0))
    # print(seq.get_raw(0))
    # print(seq.get_id(0))
    # print(seq.get_description(0))
    # print(seq.get_sequence(0))
    # print(seq.get_fasta(0))
    #
    seqgb = SeqRecordGenbank()
    seqgb.parse("sequence.gb")
    #print(fastalist)
    #
    # print("GB")
    # print(seqgb.get_gc_content(0))
    # print(seqgb.get_raw(0))
    # print(seqgb.get_id(0))
    # print(seqgb.get_description(0))
    # print(seqgb.get_sequence(0))
    # print(seqgb.get_fasta(0))

    # print(repr(seqgb))
    # print(str(seqgb))
    # print(bytes(seqgb))

    for item in seq:
        print(item)