from pprint import pprint

def fasta_parser():
    file_handle = open('sequence.fasta', 'r')
    dl = []
    for line in file_handle:
        dd= {}
        if line[0] == '>':
            id, des = line[:-1].strip('>').split(maxsplit=1)
            dd['ID'] = id
            dd['Description'] = des
            dd['raw'] = line
            dd['Sequence'] = ''
            dl.append(dd)

        else:
            Sequence = ''.join(line.split())
            dl[len(dl) - 1]['Sequence'] += Sequence
            dl[len(dl) - 1]['raw'] += line[:-1]
    return (dl)


print(fasta_parser())