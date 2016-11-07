# Entpacken: **

#x, y, z =[1, 2, 3]
z = [1, 2, 3]
#print(z)
#print(*z)

dict = {"sep": "--"}
print(**dict)

d = {'sep':'--'}
l = ["asasd", "wwewqew"]
print("asdsad","ssdsdd",**d)
print("assadsa","asdsa", *l, sep="--")

# Aufgabe 9A
#
# import time
# import io
#
# def string_repeat1(string, repeat):
#     string_io = io.StringIO(string)
#
#     for i in range(repeat):
#         string_io.write(string)
#         #print(string_io.getvalue())
#
#     #print(string_io.getvalue())
#     return string_io.getvalue()
#
# #string_repeat1("TEST, ", 10)
#
# def string_repeat2(string, repeat):
#     str_immu = ""
#
#     for i in range(repeat):
#         str_immu += string
#         #print(string)
#
#     #print(str_immu)
#     return str_immu

#string_repeat2("TEST, ", 10)

# start = time.time()
# string_repeat1("test", 100000000)
# end = time.time()
# print("Dauer von StringIO in Sekunden: {:.3}".format(end-start))
# start = time.time()
# string_repeat2("test", 100000000)
# end = time.time()
# print("Dauer von String in Sekunden: {:.3}".format(end-start))

# f = open("test", "w")
# type(f)
# f.write("Dies ist ein Test")
# print(f)
# seek = f.seek(0)
# print(seek)
#
# f.close()
# #
# f = open("test", "r")
# type(f)
# f.read()
# f.close()

# f = open("test", "w")
# f.write("Süße Träume wünsche ich dir.Heute und morgen") #Achtung welcher Zeichensatz verwendet wird. Unicode, ASCII
# f = open("test", "r")
# print(f.tell())
# s = f.read()
# print(f.tell()) # 47
# print(len(s)) # 43

# f.seek(0) # Go to position 0
# f.tell() # Ask for current position
# f.seek(2) # Go to position 2
# f.read() # UnicodeDecodeError
# f.close() # Close file handler and stream

# f = open("test", "ab")
#print(f.tell())
#f.seek(0)
#print(f.seek(0))
#f.seek(0,2)
#print(f.seek(0,2))

#print(f.peek(1))

# stream = open("stream", "rb+")
# stream.write(b"Das ist ein Stream")

