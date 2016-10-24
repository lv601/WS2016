def fasta_parser():
    total_raw = ''
    for line in open('../examples/sequence.fasta', 'r'):
        total_raw += line

    for sequence in total_raw.split('>')[1:]:
        header = sequence.partition(' ')
        curr_seq = {}
        curr_seq['raw'] = sequence
        curr_seq['sequence'] = ''.join(sequence.splitlines()[3:])
        curr_seq['id'] = header[0]
        curr_seq['description'] = header[2].split('\n')[0]
        yield curr_seq

for result in fasta_parser():
    print(result['id'],result['description'])
