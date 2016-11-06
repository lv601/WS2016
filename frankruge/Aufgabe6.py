#!/usr/bin/env python3 




from pprint import pprint

def tester(file):
	file_handle = open(file,"r")
	for line in file_handle:
		if line.startswith(">"):
			a,b,c=line[1:].split(maxsplit=2)
			print(a)
			print(b)
			print(c)

def parse_fasta(file):
	file_handle = open(file, "r")
	db =[]
	for line in file_handle:
		if line.startswith(">"):
			description, id = line[1:].split(maxsplit=1) #zwei Variablen gleichzeitig zugewiesen
			db.append({'id': id, 'description': description, 'sequence': "", 'raw': line})
		else:
			db[-1]['sequence'] += line.rstrip()
			db[-1]['raw'] += line


	pprint(db)
	print(len(db))
parse_fasta("../examples/sequence.fasta")
#tester("../examples/sequence.fasta")









#
#start = time.time()
#dab=get_raw_from_fasta(pathtofile)
#end = time.time()
#t(end-start)
#for i in range(len(dab)):
#    pprint('id = '+dab[i]['id'])
#print(str(dab[0][0]).split('|'))
#for priii in range(len(dab)):
#    print('id = '+dab[i]['id'])
#    print('raw = '+dab[i]['raw'])
#    print('description = '+dab[i]['description'])

