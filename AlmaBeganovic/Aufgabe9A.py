import io

def string_repeat1(string="Teststring", repeat=10000): #string repeat 10000 mal
    for i in range(repeat):
        string += string
    return string

def string_repeat2(string="Teststring", repeat=10000): #
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

string_repeats = stop_time(string_repeat1, repeat=5)
stream_repeats = stop_time(string_repeat2, repeat=5)