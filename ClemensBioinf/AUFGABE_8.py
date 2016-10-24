from time import time

def fasta_parser1(path):
    data = []
    total_raw = ''
    for line in open(path, 'r'):
        total_raw += line

    for sequence in total_raw.split('>')[1:]:
        header = sequence.partition(' ')
        curr_seq = {}
        curr_seq['raw'] = sequence
        curr_seq['sequence'] = ''.join(sequence.splitlines()[3:])
        curr_seq['id'] = header[0]
        curr_seq['description'] = header[2]
        data.append(curr_seq)
    return data

def fasta_parser2(path):
    data = []
    total_raw = bytearray()
    for line in open(path, 'r'):
        total_raw += str.encode(line)

    for sequence in total_raw.split(b'>')[1:]:
        header = sequence.partition(b' ')
        curr_seq = {}
        curr_seq['raw'] = bytes(sequence)
        curr_seq['sequence'] = b''.join(sequence.splitlines()[3:])
        curr_seq['id'] = header[0]
        curr_seq['description'] = header[2]
        data.append(curr_seq)
    return data

def get_time(func, *args):
    print(*args)
    start = time()
    func(*args)
    end = time()
    print("Total time ({}): {}".format(func.__name__, round(end - start, 5)))

get_time(fasta_parser2, "/home/vortex/Desktop/Bioinformatik/Programmieren/WS2016/examples/long.fasta")
get_time(fasta_parser1, "/home/vortex/Desktop/Bioinformatik/Programmieren/WS2016/examples/long.fasta")

# ANMERKUNG: Wenn ich das Programm von PyCharm ausführen lasse, scheint die Laufdauer der einzelnen Funktionen stark
# zu variieren, je nachdem welche der beiden Funktionen zuerst ausgeführt wird.
# Wenn ich also fasta_parser2 vor fasta_parser1 (bytearray) abspiele, ist fasta_parser1 fast doppelt so schnell wie
# umgekehrt (s.u.). Gibt es dafür eine einfache Erklärung?
#
# get_time(fasta_parser1, "/home/vortex/Desktop/Bioinformatik/Programmieren/WS2016/examples/long.fasta")
# get_time(fasta_parser2, "/home/vortex/Desktop/Bioinformatik/Programmieren/WS2016/examples/long.fasta")
