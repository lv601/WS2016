#!/usr/bin/env python3

## Date: 19.10.2016
## Author: Anna Majewski
## Description: Fasta Parser

import ws2016 as ws
import sys, io

def parse_console():
    if len(sys.argv) > 1: #wenn ich einen filename eingegeben habe, ist er in sys.argv[1]
        filename = io.open(sys.argv[1], mode="rb") #oeffne file als bytes.IO
        file = ws.fasta_parser(filename) #Aufruf des Parsers
        print(file) #Ausgabe der Ausgabe vom Fasta Parser
        filename.close() #Schliessen des Streams

stream = io.open("../examples/long.fasta", mode="rb")
ws.fasta_parser(stream)
