# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:29:51 2016

@author: jose
"""

string = input ("Geben Sie einen Text ein:")
ws = 3
for i in range (0, len(string) - ws + 1):
    print (" " * i, string[i:i + ws],sep="")