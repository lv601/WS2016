### Aufgabe 16a - Alexander Tolios - last modified 29.10.2016 

import pprint

class Adressbuch:
    def __init__(self):
        self.Eintragsnummer = 0        
        self.Adressbuch = []
        print("Adressbuch erzeugt")


    def add_Eintrag(self, Eintrag):
        self.Adressbuch.append(Eintrag)
        self.Eintragsnummer += 1

class Eintrag:
    def __init__(self, Vorname, Nachname, Hobbies, Alter, Geschlecht, Eigenschaften):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Hobbies = Hobbies
        self.Alter = Alter
        self.Geschlecht = Geschlecht
        self.Eigenschaften = Eigenschaften

        string = "{} {} steht jetzt in der Datenbank"
        print(string.format(self.Vorname, self.Nachname))

    def __str__(self):
        pp = pprint.PrettyPrinter(indent=2, width=10)
        return "Vorname: {0.Vorname}\nNachname: {0.Nachname}\nAlter: {0.Alter}\nHobbies: {0.Hobbies}\nGeschlecht: {0.Geschlecht}\nEigenschaften: {2}\n".format(self, ",".join(self.Hobbies), pp.pformat(self.Eigenschaften))

    def __bytes__(self):
        return self.__str__().encode()

    def __repr__(self):
        return "Eintrag von: " + self.Vorname + " " + self.Nachname


ad = Adressbuch()


Eintrag1 = Eintrag("Ferdl", "McMiller", "Python", "jung", "männlich", "g'schupft")
Eintrag1.Vorname

Eintrag2 = Eintrag("Karl-Heinz", "Gröfiaz", "den Schwiegereltern helfen", "zu jung", "männlich", "zu schön")
ad.add_Eintrag(Eintrag2)

print(Eintrag2.__dict__)
print(Eintrag2.Alter)
print(repr(Eintrag2))
print(str(Eintrag2))

