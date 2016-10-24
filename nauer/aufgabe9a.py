#!/usr/bin/env python3

""" Aufgabe 9a
Erstellen Sie zwei Funktionen, die einen String (string) und einen Integer (repeat) übernehmen.

Die Funktion soll in einer for-Schleife, die 'repeat' mal wiederholt wird, 'string' immer wieder aneinander ketten und
den entstandenen String am Ende zurückgeben.

In der ersten Funktion verwenden sie den Typ str mit dem += Operator und in der zweiten Funktion die StringIO Klasse.
Vergleichen Sie am Ende die Geschwindigkeit der beiden Funktionen.
"""

import time, io

# Use StringIO class
def string_repeat1(string="Teststring", repeat=10000):
    str_io = io.StringIO()

    for i in range(repeat):
        str_io.write(string)

    return str_io.getvalue()

# Use immutable String with += operator
def string_repeat2(string="Teststring", repeat=10000):
    str_immu = ""

    for i in range(repeat):
        str_immu += string

    return str_immu

def stop_time(func, *args, **kargs):
    start = time.time()

    result = func(*args, **kargs)

    end = time.time()
    print("Function {} takes {:.3} seconds".format(func.__name__, end-start))
    return result

res1 = stop_time(string_repeat1, repeat=5)
res2 = stop_time(string_repeat2, repeat=5)

res1 == res2

res1 = stop_time(string_repeat1, repeat=100000)
res2 = stop_time(string_repeat2, repeat=100000)

res1 = stop_time(string_repeat1, "*" * 50, repeat=100000)
res2 = stop_time(string_repeat2, "*" * 50, repeat=100000)

res1 = stop_time(string_repeat1, "*" * 500, repeat=100000)
res2 = stop_time(string_repeat2, "*" * 500, repeat=100000)

res1 = stop_time(string_repeat1, "*" * 5000, repeat=100000)
res2 = stop_time(string_repeat2, "*" * 5000, repeat=100000)
