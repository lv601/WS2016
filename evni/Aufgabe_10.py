import sys

def func(filename = None):
    if filename:
        file = open(filename, 'w')
    else:
        file = sys.stdout
    file.write('Hello World')
    file.close()
    #print('Hello World2', file = file)
func()
func('out.txt')




