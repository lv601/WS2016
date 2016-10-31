
import io

class SeqRecord:
    def __init__(self, seq, id, raw):
        self.seq = seq
        self.id = id
        self.raw = raw


class SeqRecordFasta (SeqRecord):
    def __init__(self, seq, id, raw, d):
        super().__init__(seq, id, raw)
        self.desc = d


    def __str__(self):
        result = str(self.raw.getvalue().decode())
        return result


    def __repr__(self):
        result = "SeqRecordFasta('" + str(self.seq.getvalue().decode()) + "', '" + str(self.id) + "', '" + str(self.raw.getvalue().decode()) + "', '" + str(self.desc) + "')"
        return result


    def __bytes__(self):
        result = self.raw.getvalue()
        return result


class Parser:
    def __init__ (self):
        self.list_of_dict =[]

    def pars4fasta_bytearray (self, file_handle):

        for line in file_handle:
            if line[0] == 62:                               #def erste Zeile die mit > (Dec=62, Ascii) eingeleitet wird
                id, desc = line.split(maxsplit=1)
                id = id[1:]
                desc = desc.strip()
                SRF = SeqRecordFasta(io.BytesIO(), id, io.BytesIO(line), desc)
                self.list_of_dict.append(SRF)
            else:
                sequence = line.strip()

                self.list_of_dict[-1].seq.write(sequence)
                self.list_of_dict[-1].raw.seek(0, 2)        # wichtig, da raw auch id und desc beinhalten soll
                self.list_of_dict[-1].raw.write(line)       # schreibt zeile in den stream

    def get_raw (self, index):
        return (self.list_of_dict [index].raw)

    def get_id (self, index):
        return (self.list_of_dict[index].id)

    def get_description (self, index):
        return (self.list_of_dict[index].desc)

    def get_sequence (self, index):
        return (self.list_of_dict[index].seq)