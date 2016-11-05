### Aufgabe 17a - Alexander Tolios - last modified 29.10.2016 

import pprint

class Adressbuch:
    def __init__(self):
        self.db_eintrag = []
        self.Eintragsnummer = 0
        print("Adressbuch erzeugt")

    def __getitem__(self, item):
        return self.db_eintrag[item] # getitem-Funktion - Liest Element aus Container

    def __iter__(self):
        for i in self.db_eintrag: # Iterator-Funktion (für Generator)
            yield i

    def __len__(self):
        return len(self.db_eintrag) + 1 # Anzahl der Elemente des Containers (+1, da Informatiker mit 0 zu zählen beginnen)

    def add_Eintrag(self, add_entry):
        self.db_eintrag.append(add_entry)
        self.Eintragsnummer += 1


ad = Adressbuch()



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




Eintrag1 = Eintrag("Ferdl", "McMiller", "Python", "jung", "männlich", "g'schupft")
Eintrag1.Vorname

Eintrag2 = Eintrag("Karl-Heinz", "Gröfinaz", "den Schwiegereltern helfen", "zu jung", "männlich", "zu schön")
ad.add_Eintrag(Eintrag2)

Eintrag3 = Eintrag("Gustav", "Gans", "glücklich sein", "unbekannt", "männlich", "????")
ad.add_Eintrag(Eintrag2)

# print(Eintrag2.__dict__)
# print(Eintrag2.Alter)
# print(repr(Eintrag2))
# print(str(Eintrag2))
# print(len(ad))

