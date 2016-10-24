# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:37:28 2016

@author: michi
"""

import sys

def independet_write(filename=None):
    if filename == None:
        stream = sys.stdout
    else:
        stream = open(filename, "w")
    stream.write("Hello World")

independet_write()
independet_write("foo.txt")