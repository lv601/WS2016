

class contact:
    def __init__(self, vorname, nachname, alter, hobbies, eigens):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.hobbies = hobbies
        self.eigens = eigens
        return
    def __repr__(self):
        return self.vorname
    def __str__(self):
        return self.vorname
    def __bytes__(self):
        return (self.vorname).encode()



class adressbook(contact):
    def __init__(self):
        self.entry = []
    def add(self, eintrag):
        self.entry.append(eintrag)
    def get_entry(self, index):
        return self.entry[index].__dict__
    def get_name(self, index):
        return self.entry[index].vorname, self.entry[index].nachname
    def __len__ (self):
        return len(self.entry)
    def __getitem__(self, item):
        return self.entry[item]
    def __iter__(self):
        for item in self.entry:
            yield item



a = ["anna", "tomaselli", 32, ("schwimmen", "happy", "yoga"), "braun"]
e = ['eva', 'nissner', 41, ('radfahren', 'happy', 'stricken'), 'hellbraun']
b = ['benedikt', 'tomaselli', 28, ('rauchen', 'computerspielen', 'happy'), 'schwarz']


person_list = [a,e,b]
book = adressbook()

for it in person_list:
    x = contact(*it)
    book.add(x)
    print(str(x))
    print(repr(x))
    print(bytes(x))
    print(x)

#  get data
print(book.get_entry(0))
print(book.get_name(0))

print(book.get_entry(1))
print(book.get_name(1))











"""
class A:
    def __repr__(self):
        return "A(repr)"
    def __str__(self):
        return "Ich bin vom Typ A-str"
    def __bytes__(self):
        return b"Ich bin vom Typ A-bytes"

a = A()
print(str(a))
print(repr(a))
print(bytes(a))
print(a)


__add__ - Steht für den binären + Operator
__radd__ - Steht für den binären + Operator mit
umgekehrter Operandenreihenfolge
__iadd__ - Steht für den erweiterten
Zuweisungsoperator +=

a = 1 + 2
# is equivalent to
a = (1).__add__(2)
(left)
(rightoperator)

class A:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __add__(self, other):
        print('ok')
        if isinstance(other, A):
            print('A')
            return A(self.X + other.X, self.Y + other.Y)
        elif isinstance(other, (int, float)):
            print('int, float')
            return A(self.X + other, self.Y + other)
        else:
            return NotImplemented



a = A(x=5, y=2)
b = A(x=3, y=3)
c = a + b

attrs = vars(c)
print(attrs)
print(", ".join("%s: %s" % item for item in attrs.items()))


print(c.X, c.Y) # 8 5
# schreibt noch raus ..?
# ok
# int, float
print((a + 1).X) # 6
# print((a + "1").X) # TypeError because NotImplemented
# int has no __add__(self, A)
# print((1 + a).X) # TypeError because NotImplemented

print('+=')
class A:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __iadd__(self, other):
        if isinstance(other, A):
            self.X += other.X
            self.Y += other.Y
            print('A')
            return self
        elif isinstance(other, (int, float)):
            self.X += other
            self.Y += other
            print('int, float')
            return self
        else:
            print('not impl')
            return NotImplemented

a = A(x=5, y=2)
print(vars(a))

a += 5
print(vars(a))

a += 5.5
print(vars(a))



class A:
    def __init__(self, *args):
        self.data = args
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __iter__(self):
        for item in self.data:
            yield item


a = A("Hello", "World", "!")
print(a[1])
for item in a:
    print(item)

"""