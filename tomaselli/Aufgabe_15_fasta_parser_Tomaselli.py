def generator_func(n):
    i = 1
    while i < n:
        yield i ** 2 # Creates generator
        i += 1

# gen is iterable generator object
gen = generator_func(10)
print(next(gen)) # 1st result
print(next(gen)) # next result
print(next(gen)) # and so on
print('hi')
print(next(gen))
print(next(gen))
print(next(gen))




def generator_func(n):
    i = 1
    while i < n:
        #yield i ** 2 # Creates generator
        yield i / 2
        #yield i * 2
        i += 1

# gen is iterable generator object
gen = generator_func(10)

print('print 3')

for it in gen:
    print(it)

def parse_fasta(file_name):
    file_handle = open(file_name, "r")
    db = None
    for line in file_handle:
        if line[0] == ">":
            if db: # return if db has an full entry
                yield db
            ident, desc = line[1:].strip().split(maxsplit=1)
            db = {'id': ident, 'desc': desc, 'seq': ""}
        else:
            db['seq'] += line.rstrip()
    else:
        yield db # return last entry
    print('ok')

parse_fasta('sequence.fasta')



