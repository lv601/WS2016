class Eintrag:
    def __init__(self, vorname, nachname, hobbies, alter, eigenschaften, geschlecht):
        self.vorname = vorname
        self.nachname = nachname
        self.hobbies = hobbies
        self.alter = alter
        self.eigenschaften = eigenschaften
        self.geschlecht = geschlecht

        self.eintrag = ({'Vorname':self.vorname, 'Nachname':self.nachname, 'Hobbies':self.hobbies,\
                            'Alter':self.alter, 'Eigenschaft':self.eigenschaften, 'Geschlecht':self.geschlecht})


class Adressbuch:
    def __init__(self, eintrag):
        self.eintrag = eintrag
        self.eintraege = []

    def add(self, eintrag):
        self.eintraege.append(eintrag)
        print('Eintrag hinzugefuegt: {} {}'.format(eintrag['Vorname'], eintrag['Nachname']))

    def get(self, index, key):
        return self.eintraege[index][key]


adressbuch1 = Adressbuch({})

max_mustermann = Eintrag('Max','Mustermann', 'Programmieren', '50', 'keine', 'maennlich')
adressbuch1.add(max_mustermann.eintrag)
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