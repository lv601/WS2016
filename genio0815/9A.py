import time, io

def string_repeat1(string="TestString", repeat=1000000):
    str_io = io.StringIO()

    for i in range(repeat):
        str_io.write(string)

    return str_io

def string_repeat2(string="TestString", repeat=1000000):

    str = ""
    for i in range(repeat):
        str += string

    return str

count = 100000

start = time.time()
string_repeat1(repeat=count)
end = time.time()
print("Function takes {:.3} seconds".format(end - start))

start = time.time()
string_repeat2(repeat=count)
end = time.time()
print("Function takes {:.3} seconds".format(end - start))
