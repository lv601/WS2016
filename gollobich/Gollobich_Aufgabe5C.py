# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:10:03 2016

@author: lv
"""

def Segmente(sequence, window_size):

    for i in range(0, len(sequence) - window_size + 1):

        print(" " * i, sequence[i:i + window_size], sep="")

Segmente("ATGCTTGGACCACCACCTTGTGACA", 4)