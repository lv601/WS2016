from random import randint

def run_game(bereich, versuche):
    errate=randint(*bereich)
    for i in range(versuche):
        rate=input("Guess a number between "+str(bereich[0]+" and "+str(bereich[1])+" : ")
        if rate==str(errate):
            print("Correct!")
                   break
        else:
            print("Wrong!")
                   break
        
