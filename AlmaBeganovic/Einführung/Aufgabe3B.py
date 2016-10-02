string = raw_input ("Enter your string: ")

for x in range(0, len(string)-2):
    print "We're on time %d" % (x)
    print (string[x] + string[x + 1] + string[x + 2])
    #print (string[x:x+3])