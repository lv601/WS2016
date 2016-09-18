from pprint import pprint
import time

list_of_dict = []
list_of_dict_bin = []

def pars4fasta (list_of_dict, file_path):
    file_handle = open(file_path, "r")



    for line in file_handle:
        if line[0] == ">":                               #def erste Zeile die mit > eingeleitet wird

            id, desc = line.split(maxsplit=1)      #teilt zeile beim leerzeichen; durch maxsplit definiert man wie oft
            id = id[1:]                                 # entfernt >
            desc = desc.strip()                             #entfernt linefeed, newline

            list_of_dict.append({'id': id, 'description': desc, 'sequence': "", 'raw': line}) #hängt dict an liste

        else:

            sequence = line.strip()                         #entfernt linefeed, newline, gekürzte form von sequence = line sequence= sequence.strip()


            list_of_dict[-1]['sequence']+= sequence     #[-1] ersetzt zähler; + da sequ über mehrere zeilen geht

            list_of_dict[-1]['raw']+= line                  #w.o. line da Rohdaten gewuenscht


#Wesentliche Änderungen, file binär öffnen und überall wo string war jetzt bytearray verwenden

def pars4fasta_bytearray (list_of_dict, file_path):
    file_handle = open(file_path, "rb")                 # rb,heisst binär lesen



    for line in file_handle:
        if line[0] == 62:                               #def erste Zeile die mit > (Dec=62, Ascii) eingeleitet wird

            id, desc = line.split(maxsplit=1)
            id = id[1:]
            desc = desc.strip()
            list_of_dict.append({'id': id, 'description': desc, 'sequence': bytearray(), 'raw': bytearray(line)})  # byterray() als Platzhalter ersetzt ""


        else:

            sequence = line.strip()


            list_of_dict[-1]['sequence']+= sequence

            list_of_dict[-1]['raw']+= line


# Zeit messen

start = time.time()
pars4fasta(list_of_dict, "/home/claudia/ws2016/examples/long.fasta")
end = time.time()
print("Dauer alte Methode: {:.3} seconds".format(end-start))  # 3 für 3 gültige Stellen?

start = time.time()
pars4fasta_bytearray(list_of_dict_bin, "/home/claudia/ws2016/examples/long.fasta")
end = time.time()
print("Dauer neue Methode: {:.3} seconds".format(end-start))
