#!/usr/bin/env python3

## Date: 29.10.2016
## Author: Anna Majewski
## Description: Argparser auf Aufgabe 11 angewandt.

import ws2016 as ws
import sys, io

from argparse import ArgumentParser
from argparse import FileType

def parse_console(args):
    filename = args.input # Die Eingabedatei
    file = ws.fasta_parser(filename) #Aufruf des Parsers
    if args.output == "-": # Abfrage ob output angegeben wurde
        print(file, file=sys.stdout) #Ausgabe der Ausgabe vom Fasta Parser in sys.stdout
    else:
        print(file, file=args.output) # oder Ausgabe in der angegebenen Datei.
    filename.close() #Schliessen des Streams

parser = ArgumentParser() # Konstruktor

parser.add_argument("-i", "--input", help="Eingabedatei", type=FileType("rb"), default="-")
parser.add_argument("-o", "--output", help="Ausgabedatei", type=FileType("w"), default="-")
parser.set_defaults(func=parse_console) #Funktion wird zugewiesen, die als Standard ausgefuehrt wird

args = parser.parse_args()
args.func(args) #Funktion wird mit Argumenten aufgerufen.
