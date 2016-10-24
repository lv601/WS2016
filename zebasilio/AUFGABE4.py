# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:01:05 2016

@author: jose
"""
# TIPP: Verwenden Sie für Konstanten wie diese uppercase Notation VAR1, VAR2, ...
# Sehen sie z.B. das Modul re
# import re
# re.IGNORECASE
var1 = 1
var2 = 2
var3 = 4
var4 = 8
var5 = 16
var6 = 32
var7 = 64
var8 = 128
flags = var1 | var3 | var8
print (flags) #133
for i in range(8):
    if flags & 2 **i:
        print ("flag", 2**i, "was set.")
#flag 1 was set.
#flag 4 was set.
#flag 128 was set.

