# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:50:32 2016

@author: jose
"""

import sys

def func_helloworld(filename=None):
    if filename:
        f = open(filename, "w")
    else:
        f = sys.stdout
        
    f.write("Hello World")
    f.close()


func_helloworld()
func_helloworld("HelloWorld.txt")