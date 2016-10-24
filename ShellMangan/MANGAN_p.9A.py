import time, io

def stringrep1(string="Teststring", repeat=10000):
    str_io=io.StringIO()
    for i in range(repeat):
        str_io.write(string)
    return str_io.getvalue()

def stringrep2(string="Teststring", repeat=10000):
    str_immute= ""
    for i in range(repeat):
        str_immute += string
    return str_immute

def stoptime(func, *args, **kargs):
    start=time.time()
    result=func(*args, **kargs)
    end=time.time()
    print("Function {} takes {:.3} seconds".format(func.__name__,end-start))
    return result
res1=stoptime(string_repeat1, repeat=5)
res2=stoptime(string_repeat2, repeat=5)
res1==res2
res1 = stoptime(string_repeat1, repeat=100000)
res2 = stoptime(string_repeat2, repeat=100000)
res1 = stoptime(string_repeat1, "*" * 50, repeat=100000)
res2 = stoptime(string_repeat2, "*" * 50, repeat=100000)
res1 = stoptime(string_repeat1, "*" * 500, repeat=100000)
res2 = stoptime(string_repeat2, "*" * 500, repeat=100000)
res1 = stoptime(string_repeat1, "*" * 5000, repeat=100000)
res2 = stoptime(string_repeat2, "*" * 5000, repeat=100000)
    
