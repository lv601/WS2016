import time, io

start = time.time()

def string_repeat(string="Was ist da los???\n", repeat=1000000):
    str = ""
    for i in range(repeat):
        str += string
    return str

string_repeat()

end = time.time()

print("{:.3} seconds".format(end - start))

start = time.time()

def string_repeat2(string="Was ist da los???\n", repeat=1000000):
    str_io = io.StringIO()
    for i in range(repeat):
        str_io.write(string)

    return str_io.getvalue()

string_repeat2()

end = time.time()

print("{:.3} seconds".format(end - start))
