inString = input("Please enter a string:  ")
incr = 3

print(len(inString))

for i in range(0,(len(inString)-incr+1)):
    print(inString[i:i+incr])
