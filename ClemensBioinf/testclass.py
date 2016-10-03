# Create a class
class Oligonucleotide:
    # Constructor
    def __init__(self, sequence, origin):
        self.sequence = sequence
        self.origin = origin

    # Method
    def get_len(self):
        return len(self.sequence)

# Instance
test_seq = Oligonucleotide('ATGCATGC', 'fictional')

# Assign new value to class variable
test_seq.sequence = 'ATGCATGCT'


print(test_seq.sequence)
print(test_seq.get_len())