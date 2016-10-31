# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:27:48 2016

@author: jose and ClemensBioinf
"""
import ws2016
import sys    
        

f = open(sys.argv[1], "rb")
parser = ws2016.Parser(f.read())
data = parser.fasta_parser()

try:
    index = int(sys.argV[2])
except:
    index = 0

print('{}: {}'.format(parser.get_id(data,index), parser.get_gc_content(data,index)))
