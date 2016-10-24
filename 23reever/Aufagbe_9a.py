import time
import io

def string_repeat1(string, repeat):
    string_io = io.StringIO(string)

    for i in range(repeat):
        string_io.write(string)
        #print(string_io.getvalue())

    #print(string_io.getvalue())
    return string_io.getvalue()

#string_repeat1("TEST, ", 10)

def string_repeat2(string, repeat):
    str_immu = ""

    for i in range(repeat):
        str_immu += string
        #print(string)

    #print(str_immu)
    return str_immu

#string_repeat2("TEST, ", 10)

start = time.time()
string_repeat1("test", 10000000)
end = time.time()
print("Dauer von StringIO in Sekunden: {:.3}".format(end-start))
start = time.time()
string_repeat2("test", 10000000)
end = time.time()
print("Dauer von String in Sekunden: {:.3}".format(end-start))

# Output:
# Dauer von StringIO in Sekunden: 0.843
# Dauer von String in Sekunden: 0.574