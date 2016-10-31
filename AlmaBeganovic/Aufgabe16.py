class data:
    def __init__(self, Vorname, Nachname, Hobbies, Alter, Eigenschaften, Geschlecht):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Hobbies=Hobbies
        self.Alter=Alter
        self.Eigenschaften=Eigenschaften
        self.Geschlecht=Geschlecht

        def __repr__(self):
            return "data()"

        def __str__(self):
            return "Ich bin vom Typ data "


        def __bytes__(self):
            return b"Ich bin vom Typ data"



class Adressbuch:
    def __init__(self):
        self.data = []

    def add_entry(self,data):
        self.data.append(data)

test=data("Max", "Mustermann", "Schwimmen,Tanzen und Lesen", 45, "Haarfarbe:blond", "männlich")

print(test.Alter, test.Nachname)



ad = Adressbuch()
ad.add_entry(test)


print(ad)
print(bytes(ad))
print(repr(ad))

#print(eval(repr(ad))
