import time, io

def repeat_string1(string="Teststring", repeat=10000):
    str_io=io.StringIO
    for i in range(repeat):
        str_io.write(string)
    return str_io.getvalue()

def repeat_string2(string="Teststring", repeat=10000):
    str_im = ""

    for i in range(repeat):
        str_im += string
    return str_im

def stop_time(func, args, **kwargs):
    start = time.time()
    result = func(args, **kwargs)
    end=time.time()
    print("Function {} takes {:.8} seconds".format(func.__name__, end-start))
    return result

r1=stop_time(repeat_string1, repeat=10000)
r2=stop_time(repeat_string2, repeat=10000)

