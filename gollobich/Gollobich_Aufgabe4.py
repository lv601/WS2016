# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:04:39 2016=

@author: Martin Gollobich Aufgabe 4
"""

var1 = 1
var2 = 2
var3 = 4
var4 = 8
var5 = 16
var6 = 32
var7 = 64
var8 = 128

flags = var1 | var4 | var3

print(flags)

for i in range(8):
    if flags & 2**i:
            print("flag ",2**i," was set")
            
