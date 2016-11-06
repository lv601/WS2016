class Eintrag:
    def __init__(self, vorname, nachname, hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.hobbies = hobbies
        self.eigenschaften = eigenschaften



class Adressbuch:
    def __init__(self):
        self.Einträge = []
    def eintrag_hinzufügen(self, neu):
        self.Einträge.append(neu)
    def get_new(self, index):
        return self.Einträge[index]


name1 = Eintrag('eva', 'niessner', 'laufen', 'happy')

Kontakt = Adressbuch()
Kontakt.eintrag_hinzufügen(name1)
Neu = Kontakt.get_new(0)

print(Neu.__dict__)
