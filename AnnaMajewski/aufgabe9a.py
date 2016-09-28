## Date: 27.09.2016
## Author: Anna Majewski
## Description: Vergleich zwischen String und Stream in Funktionen

import io

def str_rep(string="String", repeat=10000):
    """Ein String wird repeat mal wiederholt."""
    for i in range(repeat):
        string += string
    return string

def stream_rep(string="String", repeat=10000):
    """Ein Stream wird repeat mal wiederholt."""
    stream = io.StringIO()
    for i in range(repeat):
        stream.write(string)
    return stream.getvalue()

import time

def stop_time(func, *args, **kargs):
    start = time.time()

    result = func(*args, **kargs)

    end = time.time()
    print("Funktion {} benoetigt {:.3} Sekunden".format(func.__name__, end-start))
    return result

string_repeats = stop_time(str_rep, repeat=5)
stream_repeats = stop_time(stream_rep, repeat=5)
