# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:45:42 2016

@author: jose
"""

Addressbook = [{'Vorname': "Max", 'Nachname': "Mustermann", 'Alter': 43, 'Gechlecht': "mäannlich", 'Hobbies': ("Schwimmen", " Tanzen", "Lesen"), 'Eigenschaften': {'Gechicklichkeit': 10, 'IQ': 98, 'Gewicht': 88, 'Haarfarbe': "blond"}}]
Addressbook.append({'Vorname': "Jose", 'Nachname': "Basilio", 'Alter': 37, 'Gechlecht': "mäannlich", 'Hobbies': ("Fussball", " Fernsehen", "Lesen"), 'Eigenschaften': {'Gechicklichkeit': 19, 'IQ': 100, 'Gewicht': 100, 'Haarfarbe': "hell braun"}})
def add_contact(Adressbook, **kwargs):
    Adressbook.append(dict(**kwargs))
add_contact(Addressbook, Vorname="Mirte", Nachname="Post", Hobbies=["Hokey", "Fotografien"], Alter=28, Eigenschaften={'Gechicklichkeit': 10, 'IQ': 120}, Geschlecht="weiblich")
from pprint import pprint
pprint (Addressbook)

#[{'Alter': 43,
#  'Eigenschaften': {'Gechicklichkeit': 10,
#                    'Gewicht': 88,
#                    'Haarfarbe': 'blond',
#                    'IQ': 98},
#  'Gechlecht': 'mäannlich',
#  'Hobbies': ('Schwimmen', ' Tanzen', 'Lesen'),
#  'Nachname': 'Mustermann',
#  'Vorname': 'Max'},
# {'Alter': 37,
#  'Eigenschaften': {'Gechicklichkeit': 19,
#                    'Gewicht': 100,
#                    'Haarfarbe': 'hell braun',
#                    'IQ': 100},
#  'Gechlecht': 'mäannlich',
#  'Hobbies': ('Fussball', ' Fernsehen', 'Lesen'),
#  'Nachname': 'Basilio',
#  'Vorname': 'Jose'},
# {'Alter': 28,
#  'Eigenschaften': {'Gechicklichkeit': 10, 'IQ': 120},
#  'Geschlecht': 'weiblich',
#  'Hobbies': ['Hokey', 'Fotografien'],
#  'Nachname': 'Post',
#  'Vorname': 'Mirte'}]

