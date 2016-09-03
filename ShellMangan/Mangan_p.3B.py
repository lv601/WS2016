#Aufgabe 3B

i=input("Please input string: ")
x=0
for ch in i:
    l=i[x:x+3]
    print(l)
    x=x+1
    if len(l) == 3:
        continue
    else:
        break
