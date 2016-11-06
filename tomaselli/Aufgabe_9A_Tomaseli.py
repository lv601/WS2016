import time, io


def string_repeat1(string, repeat):
	str_io = io.StringIO()
	for it in range(repeat):
		str_io.write(string)
	print(str_io.getvalue())
	return str_io
	
	
def str_rep(string, repeat):
	str_io = []
	for it in range(repeat):
		str_io += (string)
	print(str_io)
	return str_io
	

start = time.time()
str_rep("Teststr", 10000)
end = time.time()
print("{:.3} seconds".format(end-start))


start = time.time()
string_repeat1("Teststr", 10000)
end = time.time()
print("{:.3} seconds".format(end-start))
