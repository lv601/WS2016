'''#FASTA file parser

#open files that are 'notwendig'
infile = open('/Users/Prometheus/Documents/gitclones/SS2016/PrometheusABW/sequence.fasta' , 'r') 				

# def lists / variables / dicts
temp_infile = [] # reads temporarly the file in a list
infile_lines = [] # split by line
data_object  = {} # data cage

#def functions of the program
def main():
	#define function variables
	data_object["raw"] = []
	data_object["id"] = []
	data_object["description"] = []
	data_object["sequence"] = []
	lineindex = 0	
	seqreadindex = 0	
	
	#get lines
	temp_infile = infile.read()
	#print(temp_infile)
	infile_lines = temp_infile.splitlines()
	#loop over and hang into dictionaries
	for i in infile_lines:
		if i.startswith(">"):
			data_object["raw"].append(i.split(" ")[0])
			data_object["id"].append(i.split(" ")[0][1:])
			data_object["description"].append(i.split(maxsplit=1)[1:])
			#print(i.split(" ")[0][1:])
			
			lineindex = infile_lines.index(i) # = seqidindex
			seqreadindex = lineindex + 1
			data_object["sequence"].append(infile_lines[seqreadindex])
			
		else:
			continue
			
main()
infile.close()
print(data_object)


###################################################################
###################################################################
#			VERSION B		#
###################################################################
###################################################################

#FASTA file parser

#open files that are 'notwendig'
infile = open('/Users/Prometheus/Documents/gitclones/SS2016/PrometheusABW/sequence.fasta' , 'r') 				

# def lists / variables / dicts
temp_infile = [] # reads temporarly the file in a list
infile_lines = [] # split by line
data_object  = [] # data cage

#def functions of the program
def mainb():
	#define function variables
	data_dict = {}
	lineindex = 0	
	seqreadindex = 0	
	
	#get lines
	temp_infile = infile.read()
	#print(temp_infile)
	infile_lines = temp_infile.splitlines()
	#loop over and hang into dictionaries
	for i in infile_lines:
		if i.startswith(">"):
			data_object.append(data_dict)
			
			data_dict["raw"] = i.split(" ")[0]
			data_dict["id"] = i.split(" ")[0][1:]
			data_dict["description"] = i.split(maxsplit=1)[1:]
			#print(i.split(" ")[0][1:])
			
			lineindex = infile_lines.index(i) # = seqidindex
			seqreadindex = lineindex + 1
			data_dict["sequence"] = infile_lines[seqreadindex]
			
		else:
			data_dict["sequence"] += i
			
mainb()
infile.close()
print(data_object)
'''
###################################################################
###################################################################
#			VERSION C --->>> Bytearray		#
###################################################################
###################################################################

#FASTA file parser

#open files that are 'notwendig'
infile = open('/home/michi/Dokumente/gitclones/WS2016/PrometheusABW/sequence.fasta' , 'rb') 				



# def lists / variables / dicts
temp_infile = [] # reads temporarly the file in a list
infile_lines = [] # split by line
data_object  = [] # data cage

#def functions of the program
def mainc():
	#define function variables
	data_dict = {}
	lineindex = 0	
	seqreadindex = 0	
	
	#get lines
	temp_infile = infile.read()
	#print(temp_infile)
	infile_lines = temp_infile.splitlines()
	#loop over and hang into dictionaries
	for i in infile_lines:
		if i.startswith((ord(">")):
			data_object.append(data_dict)
			
			data_dict["raw"] = i.split(" ")[0]
			data_dict["id"] = i.split(" ")[0][1:]
			data_dict["description"] = i.split(maxsplit=1)[1:]
			#print(i.split(" ")[0][1:])
			
			lineindex = infile_lines.index(i) # = seqidindex
			seqreadindex = lineindex + 1
			data_dict["sequence"] = infile_lines[seqreadindex]
			
		else:
			data_dict["sequence"] += i[:-2]
			
mainc()
infile.close()
print(data_object)
