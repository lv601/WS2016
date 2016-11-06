from time import time
import io

def repeater(string, repeat):
    result=""
    
    for i in range(repeat):
        result += string
        
    return result
    
def io_repeater(string, repeat):
    result=io.StringIO()
    
    for i in range(repeat):
        result.write(string)
        
    return result.getvalue()
    
    
string="some random text"
repeat= 1000

start=time()
repeater(string,repeat)
end=time()
print("Total time for usual string addition:{:.5f}".format(end-start))

start=time()
io_repeater(string,repeat)
end=time()
print("total time for StringIO addition: {:.5f}".format(end-start))