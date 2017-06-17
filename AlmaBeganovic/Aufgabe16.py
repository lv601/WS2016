class data:
    def __init__(self, Vorname, Nachname, Hobbies, Alter, Eigenschaften, Geschlecht):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Hobbies=Hobbies
        self.Alter=Alter
        self.Eigenschaften=Eigenschaften
        self.Geschlecht=Geschlecht

    # ACHTUNG: Einrückungsfehler
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

# INFO: Verwende diese Klausel in Bibliotheken. Dann braucht man sie nicht wegkommentieren
if __name__ == "__main__":
    test=data("Max", "Mustermann", "Schwimmen,Tanzen und Lesen", 45, "Haarfarbe:blond", "männlich")

    print(test.Alter, test.Nachname)



    ad = Adressbuch()
    ad.add_entry(test)


    print(test)
    print(bytes(test))
    print(repr(test))

    #print(eval(repr(ad))
