import time, io

def repeat_string(string, anzahl):
    string_null=""
    for i in range(anzahl):
        string_null+=string
        return string_null

def repeat_io(string, anzahl):
    str_io = io.StringIO()

    for i in range(anzahl):
        str_io.write(string)

    return str_io.getvalue()

def take_time(func, args, **kwargs):
    start = time.time()
    func(args, **kwargs)
    end=time.time()
    print("Function takes {:.8} seconds".format(end - start))

a = input("Wie oft?")

take_time(repeat_io, "asdfasdfasdf", anzahl=int(a))
take_time(repeat_string, "asdfasdfasdf", anzahl=int(a))

io.StringIO().close()