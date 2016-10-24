from pprint import pprint

def func1():
    file_handle = open('sequence.fasta','r')
    datalist = []
    for line in file_handle:
        #print(line)
        datadict = {}
        if line[0] == '>':
           ID, Descr = line[:-1].strip('>').split(maxsplit = 1)
           datadict['ID'] = ID
           datadict['Description'] = Descr
           datadict['raw'] = line 
           datadict['Sequence'] = ''
           datalist.append(datadict)
           #print(datadict)
           
        else:
            Sequence = ''.join(line.split())
            #print(Sequence)
            datalist[len(datalist)-1]['Sequence'] += Sequence
            datalist[len(datalist)-1]['raw'] += line[:-1]
    return(datalist)
print(func1())
