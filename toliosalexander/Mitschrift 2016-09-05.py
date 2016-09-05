######### Mitschrift vom 05.09.2016 #############

y = 8
z = 10 if i < 4 else 5
z # z = 5

###############

id(i)
type(i)

a = [1, 2, 3]
b = [1, 2, 3]
c = a
d = 10
e = 10

a == b # True
a is b # False, weil die ID abgefragt wird und nicht der Wert, mutables Objekt
a is c # True
d is e # True, weil ein computables / immutables Objekt, cannot be modified

f = "hallo"
g = f
f += " Welt"
f # ist "hallo Welt" (neue ID)
g # ist "hallo" (alte ID)

h = bytearray(b"Hallo") # Mutabler Datentyp
i = h
i += b" Welt"
h # ist bytearray(b"Hallo Welt")
i # ist bytearray(b"Hallo Welt")

#für tuples (als immutabler Datentyp) werden unterschiedliche IDs vergeben




l = [1, 2, 3, 4, 5, 6]

def func(liste):
    for i in range(len(liste)): # 
        print(liste.pop(0)) # Remove first item; alternativ: liste.pop(-1) -> remove last item

func(l[0:5]) # von Wert 0 (erster) bis exklusive Wert 5 (sechster)-> hier also bis Zahl 5
func(l[:]) # von der gesamten Liste
func(l) # löscht wie Werte raus wie im liste.pop-Befehl beschrieben
print(l)

#############

str = "Hallo" # Weil String ist immutabler Datentyp

def f(a):
    print(a)
    a += " Welt"
    print(a)
    
f(str)
print(str)

# # # 

str = ["Hallo"] # Jetzt ist es eine Liste

def f(a):
    print(a)
    a.append("Welt") # Kann ich machen, weil es eine Liste ist und kein STring
    print(a)

f(str)
print(str)

# # # 

str = bytearray(b"Hallo")

def f(a):
    print(a)
    a += b" Welt"
    print(a)

f(str)
print(str)


########################

# Variablen löschen "Garbage Collection" -> mit del -> ist ein keyword!


a = [1, 2, 3]
b = "Hi"
c = b
del a[1], b
print(a, b, c) # Error, weil b nicht definiert ist; a [1, 3] und c aber schon




















