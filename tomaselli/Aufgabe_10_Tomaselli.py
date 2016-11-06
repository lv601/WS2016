import sys

def hello(file_out=None):
	x = "hello world"
	if file_out == None:
		sys.stdout.write(x) 
	else:
		file = open(file_out, "w")
		file.write(x)
	
hello("hi")
hello()

