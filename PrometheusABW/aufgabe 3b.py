#print input in substrings of len 3

userin = str(input("give me the string to slice in:"))
slicelen = 3
index = 0
indexplus = 1

for i in userin:
    if len(userin) <= index+slicelen-1:
        break
    else:
        print(userin[index:index+slicelen])
        index += 1