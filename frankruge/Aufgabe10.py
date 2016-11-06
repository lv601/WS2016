
import sys

def func(filename=None):
	if filename:
		f=open(filename, "w")
	else:
		f=sys.stdout
	#makes program independent from stream origin
	f.write("hello world")
func()
func("gagu.txt")


