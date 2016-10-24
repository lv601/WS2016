from random import randint

errate = randint(1, 10)
versuche = 5

container = [1,2,3,4,5,6,7,8,9,10] 

for i in range(versuche):
	rate = input("Geben Sie eine Zahl zwischen 1 und 10 ein: ")
	print(rate)
	while int(rate) not in container:
		rate = input("Ihr Input war nicht zwischen 1 und 10. Geben Sie eine Zahl zwischen 1 und 10 ein: ")
		print(rate)
		
	if rate == str(errate):
		print("Super! Sie haben die Zahl erraten. ")
		break 
		
	if i == 4:
		print("Die gesuchte Zahl wäre gewesen: " + str(errate))
	else:
		continue

