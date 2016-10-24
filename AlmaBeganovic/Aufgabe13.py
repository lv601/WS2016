class data:
    def __init__(self, Vorname, Nachname, Hobbies, Alter, Eigenschaften, Geschlecht):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Hobbies=Hobbies
        self.Alter=Alter
        self.Eigenschaften=Eigenschaften
        self.Geschlecht=Geschlecht

class Adressbuch:
    def __init__(self):
        self.data = []

    def add_entry(self,data):
        self.data.append(data)

test=data("Max", "Mustermann", "Schwimmen,Tanzen und Lesen", 43, "Haarfarbe:blond", "männlich")

ad = Adressbuch()
ad.add_entry(test)

print(test.Alter, test.Nachname)




