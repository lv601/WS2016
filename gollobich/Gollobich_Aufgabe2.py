# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


ad=[{'Geschlecht': 'm',
    'Nachname': 'Mustermann',
    'Alter': 43,
    'Vorname': 'Max',
    'Hobbies': ('Schwimmen', 'Tanzen', 'Lesen'),
    'Eigenschaften' : {'Geschicklichkeit': 10,
                                  'IQ': 98,
                                  'Gewicht': 88,
                                  'Haarfarbe': 'blond'}}]

    
len(ad[0]["Hobbies"])
ad[0]["Eigenschaften"]["IQ"]

ad[0].keys()

ad.append({'Vorname':"Loller", 'Nachname': "Coaster",
                   'Alter': 24, 'Geschlecht': "n.a.",
                   'Hobbies': ("Radeln", "Tanzen", "Singen"),
                   'Eigenschaften' : {'Geschicklichkeit': 18,
                                      'IQ': 100,
                                      'Gewicht': 65,
                                      'Haarfarbe': 'schwarz'},
                   'Organisationen' : 'PyLadies'})

len(ad)
print(ad)