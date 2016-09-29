import time
import sys

def parse_fasta(stream, db=None):
    if not db:
        db = []

    if isinstance(stream.read(0), (bytes, bytearray)):
        for line in stream:
            if line[0] == 62:  # ord(">") bytes are stored as numbers
                # New fasta sequence starts - parse header
                ident, sep, desc = line[1:].strip().partition(b" ")

                # Create new sequence entry in db
                db.append({'id': ident,
                         'description': desc,
                         'sequence': bytearray(),  # Switch to bytearray
                         'raw': bytearray(line)})  # Switch to bytearray
            else:
                # Sequence line
                db[-1]['sequence'] += (line.rstrip())
                db[-1]['raw'] += (line)
        return db
    else:
        print("Stream must be binary", file=sys.stderr)
        exit(-1)

def get_raw(db, index):
    """
    Return original text data
    :param db:
    :param index:
    :return: str
    """
    return db[index]['raw']

def get_fasta(db, index, line_length=80):
    """
    Return sequence in fasta format
    :param db:
    :param index:
    :return: str
    """
    strings = [">{0[id]}|{0[description]}".format(db[index])]

    for i in range(0, len(db[index]['sequence']), line_length):
        strings.append(db[index]['sequence'][i:i + line_length])

    return "\n".join(strings)

def add_sequence_object(db, id, description, sequence, **features):
    """
    Add a new sequence to data dictionary
    :param db:
    :param id:
    :param description:
    :param sequence:
    :param features: Any kind of feature not mentioned in the main features
    :return: None
    """
    db.append({'id': id, 'description': description, 'sequence': sequence, **features})

def get_gc_content(db, index):
    """
    Returns the % GC content
    :param db:
    :param index:
    :return: float
    """
    seq = db[index]['sequence'].lower()
    return 100 / len(seq) * (seq.count(b"g") + seq.count(b"c"))

# Stop time of function calls
def stop_time(func, *args, **kargs):
    start = time.time()

    result = func(*args, **kargs)

    end = time.time()
    print("Function {} takes {:.3} seconds".format(func.__name__, end - start))
    return result

if __name__ == "__main__":
    # Run test code
    print(__file__)