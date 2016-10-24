class Car:
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

        string = "Ein Auto des Types {} hinzugefügt"
        print(string.format(self.type))

car1 = Car("VW whatever", 300 )

print(car1.type, car1.speed)

class Eintrag:
    def __init__(self, Vorname, Nachname, Hobbies, Alter, Eigenschaften, Geschlecht):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Hobbies = Hobbies
        self.Alter = Alter
        self.Eigenschaften = Eigenschaften
        self.Geschlecht = Geschlecht

        string = "Ein Eintrag für {} {} wurde hinzugefügt"
        print(string.format(self.Nachname, self.Vorname))

class Adressbuch:
    def __init__(self):
        self.data=[]
    def add_eintrag(self, eintrag):
        self.data.append(eintrag)
    def get_entry(self, index):
        return self.data[index].__dict__
    def get_name(self, index):
        return self.data[index].Vorname, self.data[index].Nachname

#Adressbuch=()

person1 = Eintrag("Max", "Mustermann", ("Schwimmen", "Tanzen"), 43, {"Geschicklichkeit": 10, "IQ": 98, "Gewicht": 88, "Haarfarbe": "blond"}, "Männlich")
person2 = Eintrag("Henriette", "Musterfrau", None, 23, None, "Weiblich")

ad = Adressbuch()
ad.add_eintrag(person1)
ad.add_eintrag(person2)

print(ad.get_entry(0))
print(ad.get_name(0))

print(ad.get_entry(1))
print(ad.get_name(1))