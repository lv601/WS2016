class Eintrag:
    def __init__(self, Vorname, Nachname, Alter, Geschlecht, Hobbies, Eigenschaften):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Alter = Alter
        self.Geschlecht = Geschlecht
        self.Hobbies = Hobbies
        self.Eigenschaften = Eigenschaften

    def __str__(self):
        return "Der Name des Benutzers ist " + self.Nachname + " " + self.Vorname

    def __bytes__(self):
        return b"Bytemode"

    def __repr__(self):
        return "Der Name des Benutzers ist " + self.Nachname + " " + self.Vorname

Eintrag1 = Eintrag("Mireia", "Cardenete", "25", "weiblich", "Schwimmen, Laufen, Reden", {"Geschicklichkeit": 29, "IQ": 89, "Gewicht": 60, "Haarfarbe": "braun"})
Eintrag2 = Eintrag("Eugenia", "Ruiz", "26", "weiblich", " Reisen, Reisen, Reisen", {"Geschicklichkeit": 122, "IQ": 198, "Gewicht": 160, "Haarfarbe": "dunkelbraun"})
Eintrag3 = Eintrag("Soraya", "Garcia", "24", "weiblich", "Reiten, mit Hunden spielen, Schwimmen", {"Geschicklichkeit": 11, "IQ": 55, "Gewicht": 77, "Haarfarbe": "schwarz"})

class Adressbuch:
    def __init__(self):
        self.ad = []

    def add_entry(self, Eintrag):
        self.ad.append(Eintrag)

    def get_entry(self, index):
        return self.ad[index-1]

addres = Adressbuch()
addres.add_entry(Eintrag1)
addres.add_entry(Eintrag2)
addres.add_entry(Eintrag3)

print(addres.get_entry(2).Eigenschaften['Haarfarbe'])
