#!/usr/bin/env python3    # shebang needed in executeable files. chmod a+x myfile

'''
theString=input("geben sie einen string ein: \n")
#print(len(theString))
for i in range(len(theString)):
	if(len(theString[i:i+3]) == 3):
		print(" "*i+theString[i:i+3])
	else:
		break

'''


def stringlooper(theString):
	for i in range(len(theString)):
	        if(len(theString[i:i+3]) == 3):
	                print(" "*i+theString[i:i+3])
	        else:
	                return 0

stringlooper(input("geben sie einen string ein: \n"))





