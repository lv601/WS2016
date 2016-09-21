#!/usr/bin/env python3

import sys, io


def exerc10(file=None):
    if file:
        # ACHTUNG: Wenn Sie das File so öffnen, wird es beim öffnen automatisch gelöscht ("w")
        # Sie müssen mode "r+" oder nur "r" verwenden sonst ist f.readline() immer leer
        f = open(file, "w+")
    else:
        f = sys.stdout
    f.write ("Hello World")

    if file: #Ausgabe wenn in Datei geschrieben wurde
        f.seek(0)
        print(f.readline())
        #print(f.tell())

print("Ohne Datei:")
exerc10()
print("\n\nMit Datei:")
exerc10("exerc10_test.txt")