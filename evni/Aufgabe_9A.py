import time, io


def string_repeat1(string='Test', repeat=10000):
    str_io = io.StringIO()
    for i in range(repeat):
        str_io.write(string)
    return str_io.getvalue()

def string_repeat2(string='Test', repeat=10000):
    str_immu = ''
    for i in range(repeat):
        str_immu += string
    return str_immu
    
start = time.time()
string_repeat1('Test', repeat=10000)
end = time.time()
print('Dauer StringIO sek: {:.3}'.format(end-start))

start2 = time.time()
string_repeat2('Test', repeat=10000)
end2 = time.time()
print('Dauer String sek: {:.5}'.format(end2-start2))

#Output:
#Dauer StringIO sek: 0.003
#Dauer String sek: 0.007
    
