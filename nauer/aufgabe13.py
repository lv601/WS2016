#!/usr/bin/env python3

from pprint import pprint


class Eintrag:
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.hobbies = hobbies
        self.geschlecht = geschlecht
        self.eigenschaften = eigenschaften


class Adressbuch:
    def __init__(self):
        self.Einträge = []

    def eintrag_hinzufügen(self, eintrag):
        self.Einträge.append(eintrag)


adressen = Adressbuch()

# Wrap it by a list [] to allow more entries
data = [{'vorname': "Max", 'nachname': "Mustermann",
         'alter': 43, 'geschlecht': "m",
         'hobbies': ("Schwimmen", "Tanzen", "Lesen"),
         'eigenschaften': {'Geschicklichkeit': 10,
                           'IQ': 98,
                           'Gewicht': 88,
                           'Haarfarbe': 'blond'}},
        {'vorname': "Pia", 'nachname': "Musterfrau",
         'alter': 34, 'geschlecht': "w",
         'hobbies': ("Wandern", "Tanzen", "Skydiving"),
         'eigenschaften': {'Geschicklichkeit': 9,
                           'IQ': 102,
                           'Gewicht': 68,
                           'Haarfarbe': 'brünett'}}]

adressen.eintrag_hinzufügen(Eintrag(**data[0]))
adressen.eintrag_hinzufügen(Eintrag(**data[1]))
