### Aufgabe 12b - Alexander Tolios - last modified am 29.10.2016 ###
# Subdatei ws2016 - Adaptiert


import sys, io, argparse
import fasta_parser_ta11 as fp

print(fp.__name__, "\n", fp.__file__)

db_bIO = [] # db_bIO wird leer erzeugt

# Aufruf der Funktion fasta_parser 
# fasta_parser_bIO(db_bIO, "../examples/sequence.fasta")


############### CAVE: funktioniert noch nicht! #############


def fasta_parser_test(args):
    filename = args.input # Definieren der Eingabedatei
    path = args.path # Definiert den Dateipfad
    file = fp.fasta_parser_bIO(filename) # Parseraufruf
    if args.output == "-": 
        print(file, file=sys.stdout) # Definieren der Ausgabedatei (im sys.stdout)
    else:
        print(file, file=args.output) # Definieren der Ausgabedatei
    filename.close() # Stream schliessen

parser = ArgumentParser() # von argparse

parser.add_argument("-i", "--input", help="Eingabedatei", type=FileType("rb"), default="-") # Der Hund ist hier begraben...
parser.add_argument("-p", "--path", help="Pfad", type=FileType("rb"), default="../examples/sequence.fasta") # Der Hund ist hier begraben...
parser.add_argument("-o", "--output", help="Ausgabedatei", type=FileType("w"), default="-")
parser.add_argument("-d", "--db", help="Database-Storage-Variable", default="db_bIO")
parser.set_defaults(func=fasta_parser_test) # Funktion wird zugewiesen, die als Standard ausgefuehrt wird

# Read in command line arguments
args = parser.parse_args()
args.func(args) # Std-Funktion mit Argumenten args




