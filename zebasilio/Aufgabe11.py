# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:20:58 2016

@author: jose
"""


#import ws2016 as ws
#import sys


#def parser():
#    if len(sys.argv) > 1:
#        f = open(sys.argv[1], "rb")
#        data = ws.fasta_parser(f)
#        print(data)
#        f.close()
        


import ws2016
import sys    
        

f = open(sys.argv[1], "rb")
data = ws2016.fasta_parser(f.read())

try:
    index = int(sys.argV[2])
except:
    index = 0

print('{}: {}'.format(ws2016.get_id(data,index), ws2016.get_gc_content(data,index)))

 
