# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:39:30 2016

@author: michi
"""
import io

def funcA():
    repeat = int(input("how often do you want to repeat")) 
    string = str(input("give me the string to repeat"))
    stringplus = ""    
    for n in range(repeat):
        stringplus += string
    return stringplus


def funcB():
    repeat = int(input("how often do you want to repeat")) 
    string_io = io.StringIO(input("give me the string to repeat"))
    string_io_plus = io.StringIO    
    for n in range(repeat):
        string_io_plus.write(string_io)   
    return string_io_plus.getvalue()
    

funcA()
print("stringplus")
funcB()
print(string_io_plus)