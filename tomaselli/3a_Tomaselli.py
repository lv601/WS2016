from random import randint

x = input("zahl zw 1 und 10 eingeben")

y = randint(0,9)

c = 1
	
while c < 5:

	if x == str(y):
		print('welldone')
		break	
			
	elif x != y:
		x = input("zahl zw 1 und 10 eingeben")
		c = c + 1
		continue
		
	else:
		print(x,y)

print(y)