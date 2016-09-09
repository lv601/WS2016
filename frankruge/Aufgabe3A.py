#!/usr/bin/env python3    # shebang needed in executeable files. chmod a+x myfile

from random import randint
randomNumber=randint(1,10)
userNumber=11  #initialisierung der variable
counter=0
while(randomNumber != userNumber and counter < 10):
	counter+=1
	userNumber = int(input("geben sie eine Zahl zwischen 1 und 10  ein:"))
	if(randomNumber == userNumber):
		print("richtig!")
		break
	elif(randomNumber < userNumber):
		print("falsch! zu hoch.")
	else:
		print("falsch! zu niedrig.")

print("you used up "+str(counter)+ "of 10 trials")
print("have a nice day")


