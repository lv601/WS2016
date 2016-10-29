## Date: 20.10.2016 - 29.10.2016
## Author: Anna Majewski
## Description: Magic Methods zu Aufgabe 13 hinzufuegen

class Eintrag: # Eine Klasse Eintrag wird erstellt
    def __init__(self, name, surname, hobbies, age, attributes): #enthaelt diese 5 Felder
        self.name = name
        self.surname = surname
        self.hobbies = hobbies
        self.age = age
        self.attributes = attributes

    def __str__(self):
        return "Der Name des Benutzers ist " + self.name + " " + self.surname
    # Verhalten der Klasse fuer str() geaendert.

    def __bytes__(self):
        return b"Das ist der Byte Mode" # Ausgabe bei bytes() auf Instanzen der Klasse

    def __repr__(self):
        return "Der Name des Benutzers ist " + self.name + " " + self.surname
    # Verhalten der Klasse fuer repr() geaendert, gleich zu __str__

class Adressbuch: # Eine Klasse Adressbuch wird erstellt
    def __init__(self):
        self.data =[] # eine Liste wird erstellt

    def add_entry(self, Eintrag): # Methode Eintrag hinzufuegen wird erstellt
        self.data.append(Eintrag)

    def get_entry(self, index): # Methode Eintrag auslesen wird erstellt
        return self.data[index]

## Eintrag mit Append eingefügt.

#eintrag1 = Eintrag("Hans", "Gruber", "Raub und Diebstahl", 35, "ungeduldig, schiesswuetig, flugunfaehig")

#buch = Adressbuch()
#buch.add_entry(eintrag1)
#str(eintrag1)
#print(bytes(eintrag1))
