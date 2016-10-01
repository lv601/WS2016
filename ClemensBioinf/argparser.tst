seen = []
for haplo in open('~/Desktop/HaplotypeAnalysis/haplotype_sequences.txt'):
    if haplo in seen:
        print('kaka')
    seen.append(haplo)
