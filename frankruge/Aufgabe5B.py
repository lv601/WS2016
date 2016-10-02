#!/usr/bin/env python3    # shebang needed in executeable files. chmod a+x myfile
'''
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
'''





def guess_number(randomNumber, count):
	count+=1
	if(count==10):
		return ("zu viele Versuche")
	else:
		# TIPP:Anstatt die verschiedenen Versuche rekursiv
		# aufzurufen verwenden Sie lieber eine Schleife
		userNumber = int(input("geben sie eine Zahl zwischen 1 und 10  ein:"))
		if(randomNumber == userNumber):
			print("richtig!")
			return("yippie")
		elif(randomNumber < userNumber):
			print("falsch! zu hoch.")
			guess_number(randomNumber, count)
		else:
			print("falsch! zu niedrig.")
			guess_number(randomNumber, count)


from random import randint

# TIPP: erzeugen Sie die Zufallszahl besser in der Funktion.
# Sie können den Ratebereich als Parameter übergeben z.B.:
# guess_number((1,10), 10)
randomNumber=randint(1,10)
count=0
guess_number(randomNumber, count)
print("have a nice day")


