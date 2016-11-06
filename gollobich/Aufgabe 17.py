# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:46:56 2016

@author: lv
"""

class Addresses:
    def __init__(self):
        self.entries=[]
    def add_entry(self, entry):
        self.entries.append(entry)
    def __getitem__(self, item):
        return self.add_entry[item]
    def __iter__(self):
        for item in self.add_entry:
            yield item
    def __len__(self):
        return len(self.entry)

class entry:
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname=vorname
        self.nachname=nachname
        self.alter=alter
        self.geschlecht=geschlecht
        self.hobbies=hobbies
        self.eigenschaften=eigenschaften
    def __str__(self):
        return "Vorname: {0.vorname}, Nachname: {0.nachname}, Geschlecht: {0.geschlecht}, Hobbies: {0.hobbies}, Eigenschaften: {0.eigenschaften}"
    def __bytes__(self):
        return self.__str__().encode()
    def __repr__(self):
        return "Eintrag: ('{0.vorname}', {0.nachname}',{0.geschlecht}','{0.hobbies},'{0.eigenschaften}'".format(self)


adressen = Addresses()
data = [{'vorname': "Max", 'nachname': "Mustermann",'alter': 43, 'geschlecht': "m",'hobbies': ("Schwimmen", "Tanzen", "Lesen"),'eigenschaften': {'Geschicklichkeit': 10,'IQ': 98,'Gewicht': 88,'Haarfarbe': 'blond'}},{'vorname': "Pia", 'nachname': "Musterfrau",'alter': 34, 'geschlecht': "w",'hobbies': ("Wandern", "Tanzen", "Skydiving"),'eigenschaften': {'Geschicklichkeit': 9,'IQ': 102,'Gewicht': 68,'Haarfarbe': 'br�nett'}}]

Addresses.add_entry(entry(**data[0]))
Addresses.add_entry(entry(**data[1]))
print(Addresses.entry[0])
print(bytes(Addresses.entry[0]))
print(repr(Addresses.entry[0]))
print(eval(repr(Addresses.entry[0])))