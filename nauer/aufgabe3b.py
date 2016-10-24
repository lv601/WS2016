#!/usr/bin/env python3

""" Afugabe 3b
Lesen Sie einen String mit input() ein. Durchlaufen Sie den String mit eine for-Schleife und geben Sie pro
Schleifendurchlauf jeweils einen Substring der Länge 3 aus. Starten Sie am Stringanfang und erhöhen Sie den Index pro
Schleifendurchlauf um 1.
"""

# Ask for input
string = input("Geben Sie einen Text ein: ")

# Set window size
ws = 3

# Possible number of sequences are string length - window size + 1
for i in range(0, len(string) - ws + 1):
    # " " * i - create a nice indent for each line
    print(" " * i, string[i:i + ws], sep="")
