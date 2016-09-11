# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:20:35 2016

@author: jose
"""
Addressbook = [{'Vorname': "Max", 'Nachname': "Mustermann", 'Alter': 43, 'Gechlecht': "mäannlich", 'Hobbies': ("Schwimmen", " Tanzen", "Lesen"), 'Eigenschaften': {'Gechicklichkeit': 10, 'IQ': 98, 'Gewicht': 88, 'Haarfarbe': "blond"}}]
pprint(Addressbook)
#[{'Alter': 43,
 # 'Eigenschaften': {'Gechicklichkeit': 10,
                 #   'Gewicht': 88,
                   # 'Haarfarbe': 'blond',
                    'IQ': 98},
 # 'Gechlecht': 'mäannlich',
 # 'Hobbies': ('Schwimmen', ' Tanzen', 'Lesen'),
 # 'Nachname': 'Mustermann',
  #'Vorname': 'Max'}]

Addressbook [0] ['Eigenschaften']['IQ']
#Out[76]: 98
len(Addressbook[0] ['Hobbies'])
#Out[78]: 3
Addressbook.append({'Vorname': "Jose", 'Nachname': "Basilio", 'Alter': 37, 'Gechlecht': "mäannlich", 'Hobbies': ("Fussball", " Fernsehen", "Lesen"), 'Eigenschaften': {'Gechicklichkeit': 19, 'IQ': 100, 'Gewicht': 100, 'Haarfarbe': "hell braun"}})
pprint(Addressbook)
#[{'Alter': 43,
  #'Eigenschaften': {'Gechicklichkeit': 10,
                  #  'Gewicht': 88,
                   # 'Haarfarbe': 'blond',
                    #'IQ': 98},
  #'Gechlecht': 'mäannlich',
  #'Hobbies': ('Schwimmen', ' Tanzen', 'Lesen'),
  #'Nachname': 'Mustermann',
  #'Vorname': 'Max'},
 #{'Alter': 37,
  #'Eigenschaften': {'Gechicklichkeit': 19,
   #                 'Gewicht': 100,
    #                'Haarfarbe': 'hell braun',
     #               'IQ': 100},
  #'Gechlecht': 'mäannlich',
  #'Hobbies': ('Fussball', ' Fernsehen', 'Lesen'),
  #'Nachname': 'Basilio',
  #'Vorname': 'Jose'}]

