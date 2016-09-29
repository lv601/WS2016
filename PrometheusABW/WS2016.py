# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:57:10 2016

@author: michi
"""

def mainc(infile):
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

   infile.close()
   
       return data_object

if __name__ is __main__:
    mainc()