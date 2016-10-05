import time
import sys


#from Exception import NotImplementedError

class SeqRecord:
    def __init__(self, id , seq, raw):
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
        self.records.append(record)

        # returns the index of that record
        return len(self.records) - 1

    def parse(self, stream, type="fasta"):
        # Test if stream from type binary
        if isinstance(stream.read(0), (bytes, bytearray)):
            if type == "fasta":
                db = {}
                for line in stream:
                    if line[0] == 62:  # ord(">") bytes are stored as numbers
                        if db:
                            self.records.append(SeqRecordFasta(**db))
                            db = {}

                        # New fasta sequence starts - parse header
                        ident, sep, desc = line[1:].strip().partition(b" ")

                        db = {'id': ident,
                              'description': desc,
                              'seq': bytearray(),  # Switch to bytearray
                              'raw': bytearray(line)}   # Switch to bytearray
                    else:
                        # Sequence line
                        db['seq'] += (line.rstrip())
                        db['raw'] += (line)
            else:
                raise NotImplementedError
        else:
            print("Stream must be opened as binary", file=sys.stderr)
            # Exit script with -1. Signals an error to the operationg system
            exit(-1)

    def get_raw(self, index):
        """
        Return original text data
        :param db:
        :param index:
        :return: str
        """
        return self.records[index]['raw']

    def get_fasta(self, index, line_length=80):
        """
        Return sequence in fasta format
        :param db:
        :param index:
        :return: str
        """
        print(self.records[0].desc, index)
        strings = [">{0}|{1}".format(self.records[index].id.decode(), self.records[index].desc.decode())]

        for i in range(0, len(self.records[index].seq), line_length):
            strings.append(self.records[index].seq[i:i + line_length].decode())
        return "\n".join(strings)

    def add_sequence_object(self, id, description, sequence, **features):
        """
        Add a new sequence to data dictionary
        :param db:
        :param id:
        :param description:
        :param sequence:
        :param features: Any kind of feature not mentioned in the main features
        :return: None
        """
        self.records.append({'id': id, 'description': description, 'sequence': sequence, **features})

    def get_gc_content(self, index):
        """
        Returns the % GC content
        :param db:
        :param index:
        :return: float
        """
        seq = self.records[index].seq.lower()
        return 100 / len(seq) * (seq.count(b"g") + seq.count(b"c"))

#rec = SeqRecordGenbank("id1112", "ATTGCCGTT")





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

    parser = Parser()

    with open("../examples/sequence.fasta", "rb") as f:
        parser.parse(f, type="fasta")

        print(parser.records[1].id)
        print(parser.records[2].id)
        print(parser.records[3].id)

        print(parser.get_fasta(1))

        print(parser.get_gc_content(1))


















