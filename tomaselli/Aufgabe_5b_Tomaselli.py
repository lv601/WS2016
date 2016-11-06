from random import randint



def random(y,v):
    x = input("zahl zw dem bereich eingeben")
    y = randint(**y)
        
    c = 1
        
    while c < v:
            
        if x == str(y):
            print('welldone')
            print(y)
            break
                
        elif x != y:
            x = input("zahl zw 1 und 10 eingeben")
            c = c + 1
            continue
                
        else:
            print(x,y)


b = input("bereich")
ve = input("versuche")	

random(b,ve)