import io

def str_rep(string="String", repeat=10000):
    """Ein String wird repeat mal wiederholt. string='gewuenschter string', repeat=10000 default"""
    for i in range(repeat):
        string += string
    return string

def stream_rep(string="String", repeat=10000):
    """Ein Stream wird repeat mal wiederholt. string='gewuenschter string', repeat=10000 default"""
    stream = io.StringIO()
    for i in range(repeat):
    # mit stream.write schreibt man den String in den Stream.
        stream.write(string)
    return stream.getvalue()

## 2. Aufgabe: Pruefen, welche Funktion schneller ist (time.time)
import time

def stop_time(func, *args, **kargs):
    start = time.time()

    result = func(*args, **kargs)

    end = time.time()
    print("Funktion {} benoetigt {:.3} Sekunden".format(func.__name__, end-start))
    return result

string_repeats = stop_time(str_rep, repeat=20)
stream_repeats = stop_time(stream_rep, repeat=20)