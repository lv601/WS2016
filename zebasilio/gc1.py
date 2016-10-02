#!/usr/bin/python3
#compute %GC content
# read DNA sequence from user
dna="acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaag"
#count the number of C's in DNA sequence
number_of_c=dna.count('c')
#count the number of G's in DNA sequence
number_of_g=dna.count('g')
#determine the length of the DNA sequence
dna_length=len(dna)
#compute the %GCs
gc_percentage=(number_of_c+number_of_g)*100/dna_length
print(gc_percentage)

