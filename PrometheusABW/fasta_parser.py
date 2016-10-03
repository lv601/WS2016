#! /bin/python3 

"""
Created on Thu Sep 29 19:03:57 2016

@author: michi
"""


import WS2016

filename = open('/home/michi/Dokumente/gitclones/WS2016/PrometheusABW/sequence.fasta' ,'-rb')

ReturnValue = WS2016.fasta_file_parser(filename)
print(ReturnValue)
