# Noch nicht fertig. Siehe Block 8, S14

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

    def __str__(self):
        return('Test')

ins = Eintrag('vor','nach',['keine'],5,'keine','geschl')
print(ins)
