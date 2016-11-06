import time, io

def string_IO(string, repeat):
    str_io = io.StringIO()
    for i in range(repeat):
        str_io.write(string)
    return str_io.getvalue()

def string_repeat(string, repeat):
    a=string
    for i in range(repeat):
        a+=string
    return a

def stopwatch(func, args, **kwargs):
	start=time.time()
	func(args, **kwargs)
	end=time.time()
	print("function "+func.__name__+" takes {:.8} seconds for calculation".format(end-start))

rep=input("how often?\t")
stopwatch(string_IO,"gagu",repeat=int(rep))
stopwatch(string_repeat,"gagu",repeat=int(rep))

    

