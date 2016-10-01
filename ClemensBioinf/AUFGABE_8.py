from time import time

def fasta_parser(path):
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


start = time()
print(type(fasta_parser("/home/vortex/Desktop/Bioinformatik/Programmieren/WS2016/examples/sequence.fasta")))
end = time()
print("Total time: {}".format(round(end-start, 5)))