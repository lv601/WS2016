#!/usr/bin/env python3

""" Aufgabe 5c
Schreiben Sie die Schleife von Aufgabe 3b so um damit sie eine Funktion verwenden
"""

def get_segments(sequence, window_size, fill=" "):
    # Possible number of seqs are string length - window size + 1
    for i in range(0, len(sequence) - window_size + 1):
        # " " * i - create a nice indent for each line
        print(fill * i, sequence[i:i + window_size], sep="")

get_segments("ATGCTTGGACCACCACCTTGTGACA", 4)
get_segments("ATGCTTGGACCACCACCTTGTGACA", 4, "")
get_segments("ATGCTTGGACCACCACCTTGTGACA", 4, "*")
get_segments("ATGCTTGGACCACCACCTTGTGACA", 4, "*_")