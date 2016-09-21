import time, io

def string_repeat1(string="Teststring", repeat=10000):
    str_temp = ""
    for i in range(repeat):
        str_temp += string
    return str_temp

def string_repeat2(string="Teststring", repeat=10000):
    str_io = io.StringIO(string)
    for i in range(repeat):
        str_io.write(string)
    return str_io.getvalue()

def mytimer(func, *args, **kargs):
    import time
    start = time.time()
    result = func(*args, **kargs)
    end = time.time()
    return "{:.3}".format(end-start)

print("Start - 50 Chars / 10 Durchläufe")
print("Datatype(String):", mytimer(string_repeat1,string="*"*50, repeat=10))
print("Datatype(StringIO):", mytimer(string_repeat2, string="*"*50, repeat = 10))
print("Ende")

print("Start - 5000 Chars / 50.000 Durchläufe")
print("Datatype(String):", mytimer(string_repeat1, string="*"*5000, repeat = 50000))
print("Datatype(StringIO):", mytimer(string_repeat2, string="*"*5000, repeat = 50000))
print("Ende")