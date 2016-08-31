#Ranges
def ranges():
    r=list(range(10))
    l=list(range(1,10,3))
    print(r, l)

#for loops with ranges
def loops():
    for i in range(10):
        print(i)
    for i in range(5,10):
        print(i)


#with else
def elses():
    for i in range(5,10):
        print(i)
    else:
        print("End")

#while
def whiles():
    i=0
    while i <10:
        print(i)
        i=i+1
    else:
        print("End")

#enumerate
def enumerate():
    index=0
    my_list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
    for item in my_list:
        print(index, item)
        index=index+1
        if index >3:
            break
#breaks
def breaks():
    for i in range(10):
        if i % 2==0:
            continue
        if i ==7:
            break
        print(i)
    else:
        print("End")
