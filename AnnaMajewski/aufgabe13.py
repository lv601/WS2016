## Date: 03.10.2016
## Author: Anna Majewski
## Description: Einführung in Klassen

class Eintrag: # Eine Klasse Eintrag wird erstellt
    def __init__(self, name, surname, hobbies, age, attributes): #enthaelt diese 5 Felder
        self.name = name
        self.surname = surname
        self.hobbies = hobbies
        self.age = age
        self.attributes = attributes

class Adressbuch: # Eine Klasse Adressbuch wird erstellt
    def __init__(self):
        self.data =[] # eine Liste wird erstellt

    def add_entry(self, Eintrag): # Methode Eintrag hinzufuegen wird erstellt
        self.data.append(Eintrag)

    def get_entry(self, index): # Methode Eintrag auslesen wird erstellt
        return self.data[index]

## Eintrag mit Append eingefügt.

eintrag1 = Eintrag("Hans", "Gruber", "Raub und Diebstahl", 35, "ungeduldig, schiesswuetig, flugunfaehig")

ad = Adressbuch()
ad.add_entry(eintrag1)
blabla = ad.get_entry(0)
print(blabla.__dict__)
print(eintrag1.hobbies)
