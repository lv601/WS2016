class Eintrag:
    def __init__(self, adressbuch, vorname, nachname, hobbies, alter, eigenschaften, geschlecht):
        self.adressbuch = adressbuch
        self.vorname = vorname
        self.nachname = nachname
        self.hobbies = hobbies
        self.alter = alter
        self.eigenschaften = eigenschaften
        self.geschlecht = geschlecht

    def eintrag_hinzufuegen(self):
        self.adressbuch.add({'Vorname':self.vorname, 'Nachname':self.nachname, 'Hobbies':self.hobbies,\
                            'Alter':self.alter, 'Eigenschaft':self.eigenschaften, 'Geschlecht':self.geschlecht})
        return('{} {} hinzugefuegt'.format(self.vorname, self.nachname))

class Adressbuch:
    def __init__(self, eintrag):
        self.eintrag = eintrag
        self.eintraege = []

    def add(self, eintrag):
        self.eintraege.append(eintrag)

    def get(self, index, key):
        return self.eintraege[index][key]


adressbuch1 = Adressbuch({})

max_mustermann = Eintrag(adressbuch1, 'Max','Mustermann', 'Programmieren', '50', 'keine', 'maennlich')
max_mustermann.eintrag_hinzufuegen()
print(adressbuch1.get(0, 'Alter'))








# Adressbuch = [{
#     "Vorname": "Max",
#     "Nachname": "Mustermann",
#     "Hobbies": ["Schwimmen", "Tanzen", "Lesen"],
#     "Alter": 43,
#     "Eigenschaften": {
#         "Geschicklichkeit": 10,
#         "IQ": 98,
#         "Gewicht": 88,
#         "Haarfarbe": "blond"
#         },
#     "Geschlecht": "maennlich"
#     }]