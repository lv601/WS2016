
class contact:
    def __init__(self, vorname, nachname, alter, hobbies, eigens):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.hobbies = hobbies
        self.eigens = eigens
        return


class adressbook(contact):
    def __init__(self):
        self.entry = []
    def add(self, eintrag):
        self.entry.append(eintrag)
    def get_entry(self, index):
        return self.entry[index].__dict__
    def get_name(self, index):
        return self.entry[index].vorname, self.entry[index].nachname

a = ["anna", "tomaselli", 32, ("schwimmen", "happy", "yoga"), "braun"]
e = ['eva', 'nissner', 41, ('radfahren', 'happy', 'stricken'), 'hellbraun']
b = ['benedikt', 'tomaselli', 28, ('rauchen', 'computerspielen', 'happy'), 'schwarz']


person_list = [a,e,b]
book = adressbook()

for it in person_list:
    x = contact(*it)
    book.add(x)


#  get data
print(book.get_entry(0))
print(book.get_name(0))

print(book.get_entry(1))
print(book.get_name(1))











"""
print(book.get_entry(0).alter)
print(y.alter)
print(z.alter)

#
attrs = vars(book.get_entry(0))
print(attrs)

#
attrs = vars(x)
print(", ".join("%s: %s" % item for item in attrs.items()))

attrs = vars(y)
print(", ".join("%s: %s" % item for item in attrs.items()))

attrs = vars(z)
print(", ".join("%s: %s" % item for item in attrs.items()))


"""
