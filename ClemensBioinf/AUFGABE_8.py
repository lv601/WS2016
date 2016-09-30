from time import time

def fasta_parser(path):
    data = []
    total_raw = bytearray(b"")
    for line in open(path, "r"):
        line_bytearray = bytearray(str.encode(line))
        total_raw += line_bytearray

    for sequence in total_raw.split(b">")[1:]:
        header = True
        curr_seq = {}
        curr_seq["raw"] = bytearray(b"")
        curr_seq["sequence"] = bytearray(b"")
        for line in sequence.split(b"\n"):
            if header is True:
                curr_seq["id"] = line.split(b" ")[0]
                curr_seq["description"] = b" ".join(line.split(b" ")[1:])
                header = False
            else:
                curr_seq["sequence"] += line

            curr_seq["raw"] += line

        data.append(curr_seq)

    return data

start = time()
fasta_parser("/home/vortex/Desktop/Bioinformatik/Programmieren/WS2016/examples/sequence.fasta")
end = time()
print("Total time: {}".format(round(end-start, 5)))