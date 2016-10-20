#!/usr/bin/env python3
""" Aufgabe 2
Erstellen Sie ein Dictionary das folgende Datensatz speichern kann

Adressbuch:
  Vorname: Max
  Nachname: Mustermann
  Hobbies: Schwimmen, Tanzen, Lesen
  Alter: 43
  Eigenschaften:
    Gechicklichkeit: 10
    IQ: 98
    Gewicht: 88
    Haarfarbe: blond
  Gechlecht: männlich
"""

# Wrap it by a list [] to allow more entries
Adressbuch = [{'Vorname':"Max", 'Nachname': "Mustermann",
               'Alter': 43, 'Geschlecht': "m",
               'Hobbies': ("Schwimmen", "Tanzen", "Lesen"),
               'Eigenschaften' : {'Geschicklichkeit': 10,
                                  'IQ': 98,
                                  'Gewicht': 88,
                                  'Haarfarbe': 'blond'}}]

# For a nice print out
from pprint import pprint
pprint(Adressbuch)

Adressbuch[0]['Eigenschaften']['IQ']
len(Adressbuch[0]['Hobbies'])

Adressbuch.append({'Vorname':"Pia", 'Nachname': "Musterfrau",
                   'Alter': 34, 'Geschlecht': "w",
                   'Hobbies': ("Wandern", "Tanzen", "Skydiving"),
                   'Eigenschaften' : {'Geschicklichkeit': 9,
                                      'IQ': 102,
                                      'Gewicht': 68,
                                      'Haarfarbe': 'brünett'},
                   'Organisationen' : 'PyLadies'})

pprint(Adressbuch)

len(Adressbuch)
