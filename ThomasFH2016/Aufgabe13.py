from pprint import pprint

class Adresse:
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.hobbies = hobbies
        self.geschlecht = geschlecht
        self.eigenschaften = eigenschaften

class Adressbuch:
    def __init__(self):
        self.Adressen = []

    def Neue_Adresse(self, Adresse):
        self.Adressen.append(Adresse)
