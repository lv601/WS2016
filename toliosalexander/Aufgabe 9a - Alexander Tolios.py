### Aufgabe 9a - Alexander Tolios - last modified am 29.10.2016 ###

import time, io

# Use immutable String with += operator
def string_repeat(string, repeats):
    str_immu = ""
    for i in range(repeats):
        string += string
    return string

# Use StringIO class
def steam_repeat(string, repeats): # String wird (als Steam) repeats mal wiederholt
    str_io = io.StringIO()
    for i in range(repeats):
        str_io.write(string)
    return str_io.getvalue()

# Funktion: Zeit wird berechnet
def comp_time(func, *args, **kargs):
    start = time.time()
    result = func(*args, **kargs)
    end = time.time()
    print("Funktion {} braucht \t {:.2} Sekunden".format(func.__name__, end-start))
    return result

repeats = input("Anzahl der Wiederholungen: ")
string = input("Zu wiederholender String: ")


time_with_strings = comp_time(string_repeat, string, repeats = int(repeats))
time_with_streams = comp_time(steam_repeat, string, repeats = int(repeats))
