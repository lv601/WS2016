x = 1 # Global (Module) scope

def func():
    x = 20 # Function scope
    print(x)

print(x)
func()
print(x)

print('#########################')

####################
x = 1
print(x)

for x in range(10):
    y = x

print(x)
print(y) # Although defined in loop it is in global scope
print('#########################')
######################

a = "I'm global"

def funcA():
    print(a)

funcA()
print(a)
print('#########################')

######################
a = "I'm global"
def funcA():
    a = "New assign from funcA()"
    print(a)

funcA()
print(a)
print('#########################')

######################
a = "I'm global"
def funcA():
    global a # Use variable from global instead from local scope
    print(a)
    a = "New assign from funcA()"

funcA()
print(a)
print('#########################')

######################

a = "I'm global"

def funcA():
    b = 5
    def funcB():
        global a
        nonlocal b # Change var from enclosing function
        a = "New assign from funcB()"
        b = 2 * b

    print(a,b)
    funcB()
    print(a,b)

funcA()
print('#########################')

######################
a = "I'm global"
b = "I'm also global"

def funcA():
    b = "I'm nonlocal"
    def funcB():
        print(a, b)
    funcB()

funcA()
print(a, b)
print('#########################')

######################
print("Die LF Escapesequenz \\n")
print(r"Die LF Escapesequenz \n")
print(R"Viele \\\\ im Text")



#print(len(rawData))

    #dictFields = ['id', 'description', 'sequence', 'features']
    #inGbFile = ['ACCESSION', 'DEFINITION', 'ORIGIN', 'FEATURES']
    #occurrence =[]

    #for i in range(len(inGbFile)):
    #    occ = rawData[0].find(inGbFile[i])
    #    occurrence.append(occ)
    #    print("{}".format(occ))

    #lookUp = sorted(zip(dictFields, inGbFile, occurrence), key=lambda number: number[2])

    #lookUp.append(("", 'LOCUS', ""))

    #print(lookUp)
    #print(lookUp[0][0])

    #test=[]
    #for i in range(len(lookUp)-1):
    #    test.append((lookUp[i][0], lookUp[i][1], lookUp[i+1][1]))


    #print(test)