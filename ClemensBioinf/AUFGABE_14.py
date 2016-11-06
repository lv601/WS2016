# Equivalent zu Aufgabe 11 fuer Parser-Klasse statt Parser-Funktion
# siehe ws2016.py
import ws2016
import sys

file = open(sys.argv[1],'rb')
parser = ws2016.Parser(file.read())
data = parser.fasta_parser()

# Falls kein Index angegeben, wird erstes Fasta-File prozessiert
try:
    index = int(sys.argv[2])
except:
    index = 0

# Gewuenschte Funktion muss hier eingegeben werden
print('{}: {}'.format(parser.get_id(data,index), parser.get_gc_content(data,index)))
