from argparse import FileType as parse
from Aufgabe5B.py import guess_number
parse(guess_number(1,input("range?"))


def guess_number(randomNumber, count):
        count+=1
        if(count==10):
                return ("zu viele Versuche")
        else:
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
randomNumber=randint(1,10)
count=0
guess_number(randomNumber, count)
print("have a nice day")




