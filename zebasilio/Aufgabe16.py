# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:50:15 2016

@author: jose and ClemensBioinf
"""

c# Teil A
# Erweitertung der Eintrag-Klasse aus Aufgabe 13

class Eintrag:
    def __init__(self, vorname, nachname, hobbies, alter, eigenschaften, geschlecht):
        self.vorname = vorname
        self.nachname = nachname
        self.hobbies = hobbies
        self.alter = alter
        self.eigenschaften = eigenschaften
        self.geschlecht = geschlecht

        self.eintrag = ({'Vorname':self.vorname, 'Nachname':self.nachname, 'Hobbies':self.hobbies,'Alter':self.alter,\
                         'Eigenschaft':self.eigenschaften, 'Geschlecht':self.geschlecht})

    def __str__(self):
        # Fuer Attribute mit mehreren Punkten
        def multi_format(attribute):
            multi_format = '\n'
            for element in attribute:
                multi_format += '\t- {}\n'.format(element)
            return multi_format.rstrip('\n')

        return 'Instanz der Klasse: Eintrag\n===========================\nVorname: {0.vorname}\nNachname: {0.nachname}\
        \nHobbies: {1}\nAlter: {0.alter}\nEigenschaften: {2}\nGeschlecht: {0.geschlecht}\n==========================='\
        .format(self, multi_format(self.hobbies), multi_format(self.eigenschaften))

    def __bytes__(self):
        return self.__str__().encode()

    def __repr__(self):
        return "Eintrag('{0.vorname}', '{0.nachname}', '{0.hobbies}', '{0.alter}', {0.eigenschaften}, {0.geschlecht})"\
            .format(self)

    def __getitem__(self, attribute):
        return self.eintrag[attribute]

    def __iter__(self):
        for element in self.eintrag:
            return self.eintrag[element]

    def __len__(self):
        return len(self.eintrag)


ins = Eintrag('Max','Mustermann',['Wandern','Laufen','Malen'],20,['humorvoll','selbstlos'],'maennlich')

print(ins)
print(repr(ins))


# Teil B
# siehe ws2016.py
