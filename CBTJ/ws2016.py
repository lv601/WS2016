
import io

def pars4fasta_bytearray (list_of_dict, file_handle):




    for line in file_handle:
        if line[0] == 62:                               #def erste Zeile die mit > (Dec=62, Ascii) eingeleitet wird

            id, desc = line.split(maxsplit=1)
            id = id[1:]
            desc = desc.strip()
            list_of_dict.append({'id': id, 'description': desc, 'sequence': io.BytesIO(), 'raw': io.BytesIO(line)})  # byterray() als Platzhalter ersetzt ""

            #list_of_dict[-1].read()



        else:

            sequence = line.strip()


            list_of_dict[-1]['sequence'].write(sequence)

            list_of_dict[-1]['raw'].write(line)




def get_raw (list, index):
    return (list [index] ['raw'])
#print (get_raw (list_of_dict, 5))

def get_id (list, index):
    return (list [index] ['id'])
#print (get_id (list_of_dict, 5))

def get_description (list, index):
    return (list [index] ['description'])
#print (get_description (list_of_dict, 5))

def get_sequence (list, index):
    return (list [index] ['sequence'])

if __name__== "__main__":
	print(__file__)