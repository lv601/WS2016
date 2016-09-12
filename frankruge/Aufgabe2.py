#!/usr/bin/env python3    # shebang needed in executeable files. chmod a+x myfile

Adressbook = [{'Vorname':"Max",
               'Nachname': "Mustermann",
               'Alter': 43,
               'Geschlecht': "m",
               'Hobbies': ("Schwimmen", "Tanzen", "Lesen"), #liste
               'Eigenschaften' : {'Geschicklichkeit': 10,
                                  'IQ': 98,
                                  'Gewicht': 88,
                                  'Haarfarbe': 'blond'}}]

# For a nice print out
from pprint import pprint
pprint(Adressbook)


#Adressbuchabfrage
Adressbook[0]['Eigenschaften']['IQ']

#length function len()
print('len(Adressbook) = '+str(len(Adressbook)))

Adressbook.append({'Vorname':"Pia",
                   'Nachname': "Musterfrau",
                   'Alter': 34,
                   'Geschlecht': "w",
                   'Hobbies': ("Wandern", "Tanzen", "Skydiving"),
                   'Eigenschaften' : {'Geschicklichkeit': 9,
                                      'IQ': 102,
                                      'Gewicht': 88,
                                      'Haarfarbe': 'blond'}})

pprint(Adressbook[0]['Vorname']+' '+str(Adressbook[0]['Eigenschaften']['IQ'])+' '+str(Adressbook[0]['Hobbies'][0]))
pprint(Adressbook[1]['Vorname']+' '+str(Adressbook[1]['Eigenschaften']['IQ'])+' '+str(Adressbook[1]['Hobbies'][0]))
print('len(Adressbook) = '+str(len(Adressbook)))

def neuerKontakt(Adressbuch,**kwargs):
    Adressbuch.append(dict(**kwargs))
neuerKontakt(Adressbook, sdfsdg='fff')
print('add contact over function')
print('len(Adressbook) = '+str(len(Adressbook)))
