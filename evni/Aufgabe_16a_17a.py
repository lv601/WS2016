class Eintrag:
    def __init__(self, vorname, nachname, hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.hobbies = hobbies
        self.eigenschaften = eigenschaften

    def __str__(self):
        return 'Username: ' + self.vorname + ' ' + self.nachname

    def __bytes__(self):
        return b'Ausgabe in Bytes'

    def __repr__(self):
        return 'Username: ' + self.vorname + ' ' + self.nachname



class Adressbuch:
    def __init__(self):
        self.Einträge = []

    def __getitem__(self, item):
        return self.Einträge[item]

    def __iter__(self):
        for i in self.Einträge:
            return self.Einträge[i]

    def __len__(self):
        return len(self.Einträge)
        
    def eintrag_hinzufügen(self, neu):
        self.Einträge.append(neu)
        
    def get_new(self, index):
        return self.Einträge[index]


name1 = Eintrag('eva', 'niessner', 'laufen', 'happy')
#print(name1)
print(repr(name1))

Kontakt = Adressbuch()
Kontakt.eintrag_hinzufügen(name1)
Neu = Kontakt.get_new(0)

print(Neu.__dict__)
