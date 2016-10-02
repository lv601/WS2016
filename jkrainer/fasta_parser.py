import sys
import ws2016

stream = open(sys.argv[1], "r")
#ws2016.parse_fasta_binary(stream)

#ws2016.parse_fasta(stream)

ws2016.take_time(ws2016.parse_fasta, stream) #starte die Funktion parse_fasta innerhalb der Funktion take_time um die Zeit zu stoppen.
ws2016.take_time(ws2016.parse_fasta_binary, stream)