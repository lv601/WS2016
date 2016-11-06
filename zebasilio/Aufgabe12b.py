# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:50:17 2016

@author: jose
"""
#/usr/bin/env/python3


import ws2016 as ws
import sys
from argparse import ArgumentParser
from argparse import FileType


def parse_console(args):
    filename = args.input #the input file
    file = ws.fasta_paster(filename) # calling the Parser
    if args.output == "-": #query wether output was specified
        print(file, file=sys.stdout) #output the output from the fasta parser in sys.stdout
    else:
        print(file, file=args.output) # or output in the specified file
    filename.close()
    

parser = ArgumentParser() # constructor

parser.add_argument('-i', '--input', help='input file', type=FileType('rb'), default='-')
parser.add_argument('-o', '--output', help='output file', type=FileType('w'), default='-')
parser.set_defaults(func=parse_console) # function is assigned, which is executed as a standard


args = parser.parse_args()
parse_console(args) # function is called with arguments