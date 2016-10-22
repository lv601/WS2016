def fasta_parser(n):
    data = []
    total_raw = ''
    for line in open('../examples/sequence.fasta', 'r'):
        total_raw += line

    i = 1
    while i < n:
        for sequence in total_raw.split('>')[1:]:
            header = sequence.partition(' ')
            curr_seq = {}
            curr_seq['raw'] = sequence
            curr_seq['sequence'] = ''.join(sequence.splitlines()[3:])
            curr_seq['id'] = header[0]
            curr_seq['description'] = header[2].split('\n')[0]
            data.append(curr_seq)
        yield data[i + 1]
        i += 1

for result in fasta_parser(5):
    print(result['id'],result['description'])
