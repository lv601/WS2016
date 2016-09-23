import time
import io

def NeunA1 (s, repeat):
    result=""
    for i in range(repeat):
            result += s
    return result

def NeunA2 (s, repeat):
    result=io.StringIO()
    for i in range (repeat):
        result.write(s)
    return result.getvalue()




start = time.time()
a=NeunA1("Hope should be a controled substance", 1000000)
end = time.time()
print("Dauer alte Methode: {:.3} seconds".format(end-start))  # 3 für 3 gültige Stellen?

start = time.time()
b=NeunA2 ("Hope should be a controled substance", 1000000)
end = time.time()
print("Dauer neue Methode: {:.3} seconds".format(end-start))


