# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:05:16 2016

@author: jose
"""

def sequence(seq, size):
    for i in range(0, len(seq) - size +1):
        print (" " * i, seq[i:i + size], sep="")
sequence("ATGTGACTAGCTATATCC", 3)
        