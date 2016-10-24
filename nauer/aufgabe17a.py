#! /usr/bin/env python3

""" Aufgabe 17a
Fügen Sie die 3 spezial Methoden __getitem__(), __iter__() und __len__() der Eintrag Klasse aus Aufgabe 16a hinzu.
"""

import pprint


class Eintrag:
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.hobbies = hobbies
        self.geschlecht = geschlecht
        self.eigenschaften = eigenschaften

    def __str__(self):
        pp = pprint.PrettyPrinter(indent=2, width=10)
        return "Vorname: {0.vorname}\nNachname: {0.nachname}\nAlter: {0.alter}\nHobbies: {1}\nGeschlecht: {0.geschlecht}\nEigenschaften: {2}\n".format(self, ",".join(self.hobbies), pp.pformat(self.eigenschaften))

    def __bytes__(self):
        return self.__str__().encode()

    def __repr__(self):
        return "Eintrag('{0.vorname}', '{0.nachname}', '{0.alter}', '{0.geschlecht}', {0.hobbies}, {0.eigenschaften})".format(self)


class Adressbuch:
    def __init__(self):
        self.Einträge = []

    def __getitem__(self, item):
        return self.Einträge[item]

    def __iter__(self):
        for item in self.Einträge:
            yield item

    def __len__(self):
        return len(self.Einträge)

    def eintrag_hinzufügen(self, eintrag):
        self.Einträge.append(eintrag)

# Run examples
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

for eintrag in adressen:
    print(eintrag)

print(adressen[1].vorname)

print(len(adressen))