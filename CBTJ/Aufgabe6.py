
from pprint import pprint
list_of_dict = []



def pars4fasta (list_of_dict, file_path):
    file_handle = open(file_path, "r")

    # TIPP: zaehler wird nicht gebraucht. Auf das letzte Element in einer Liste
    # können Sie einfach mit dem ersten negativen Index zugreifen
    # list_of_dict[-1]['sequence']+= sequence
    zaehler = -1                                         # -1 Anzahl der Dict. in Liste

    for line in file_handle:
        if line[0] == ">":                               #def erste Zeile die mit > eingeleitet wird

            id, desc = line.split(" ", maxsplit=1)      #teilt zeile beim leerzeichen; durch maxsplit definiert man wie oft
            id = id[1:]                                 # entfernt >
            desc = desc.strip()                             #entfernt linefeed, newline

            list_of_dict.append({'id': id, 'description': desc, 'sequence': "", 'raw': line}) #hängt dict an liste

            zaehler +=1

        else:
            # TIPP: Kann gekürzt werden
            # sequence = line.strip()                         #entfernt linefeed, newline
            sequence = line
            sequence = sequence.strip()                         #entfernt linefeed, newline


            list_of_dict[zaehler]['sequence']+= sequence     #[zaehler] def. welches dict.; + da sequ über mehrere zeilen geht

            list_of_dict[zaehler]['raw']+= line                  #w.o. line da Rohdaten gewuenscht




pars4fasta(list_of_dict, "/home/claudia/ws2016/examples/sequence.fasta")
