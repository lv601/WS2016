print("codons - reading frames")
string = input("Geben Sie einen Text ein: ")
string2 = ("CTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCATAAG")

ws = 3

for i in range(0, len(string) - ws + 1):
	print( " " * i, string[i:i + ws], sep='')
	
for i in range(0, len(string2) - ws + 1):
	print( " " * i, string2[i:i + ws], sep='')
