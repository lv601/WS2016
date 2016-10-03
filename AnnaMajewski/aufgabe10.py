## Date: 02.10.2016
## Author: Anna Majewski
## Description: Uebergabe von Filename oder Standardoutput

import sys

def writer(filename=None):
    """Writer writes "Hello World" into a file or in standard out"""
    if filename:
        file = open(filename, w)
    else:
        file = sys.stdout
#print nutzt standard file = sys.stdout, wir geben ihm die vom user ausgesuchte Auswahl
    print("Hello World", file=file)

writer()
