
# Initialisierung der Klasse, in die einzelne Eintraege zuerst geladen werden
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


# Initialisierung der Klasse, in der saemtliche Eintraege gespeichert werden
class Adressbuch:
    def __init__(self, eintrag):
        self.eintrag = eintrag
        self.eintraege = []

    # Methode zum Uebertragen von Eintraegen ins Adressbuch
    def add(self, eintrag):
        self.eintraege.append(eintrag)
        print('Eintrag hinzugefuegt: {} {}'.format(eintrag['Vorname'], eintrag['Nachname']))

    # Methode um Eintraege abzurufen
    def get(self, index, key=None):
        if key == None: # Ganzen Eintrag einer Person abrufen
            for attribute in self.eintraege[index]:
                print(attribute, self.eintraege[index][attribute])
            return self.eintraege[index]
        else: # Einen Attribut einer Person abrufen
            print(self.eintraege[index][key])
            return self.eintraege[index][key]

# Erstellen der Adressbuch-Instanz
adressbuch1 = Adressbuch({})

max_mustermann = Eintrag('Max','Mustermann', 'Programmieren', '50', 'keine', 'maennlich')
#Holger_Maserati= Eintrag(vorname='Holger', nachname='Maserati', alter='34')
adressbuch1.add(max_mustermann.eintrag)
adressbuch1.get(0, 'Hobbies')



