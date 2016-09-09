#!/usr/bin/env python3    # shebang needed in executeable files. chmod a+x myfile

#from Aufgabe5_functions import add_contact

def add_contact(dictionary, **kwargs):
        dictionary.append(**kwargs)


##############fehlermeldung
##############
'''
Traceback (most recent call last):
  File "./Aufgabe5A.py", line 30, in <module>
    add_contact(Adressbook, Nachname="Xi") 
  File "./Aufgabe5A.py", line 6, in add_contact
    dictionary.append(**kwargs)
TypeError: append() takes no keyword arguments
'''
#############
############



Adressbook=[]


#Adressbook = [{'Vorname':"Max", 'Nachname': "Mustermann",'Alter': 43, 'Geschlecht': "m",'Hobbies': ("Schwimmen", "Tanzen", "Lesen"), 'Eigenschaften' : {'Geschicklichkeit': 10,'IQ': 98,'Gewicht': 88,'Haarfarbe': 'blond'}}]

# For a nice print out
from pprint import pprint
pprint(Adressbook)


#Adressbuchabfrage
#Adressbook[0]['Eigenschaften']['IQ']

#length function len()
#len(Adressbook[0]['Hobbies'])
#######################
add_contact(Adressbook, Nachname="Xi") 
print(Adressbook)
########################

#[print(Adressbook[i]['Vorname']) for i in range(len(Adressbook))]

#Adressbook.append({'Vorname':"Pia", 'Nachname': "Musterfrau",
#                   'Alter': 34, 'Geschlecht': "w",
#                   'Hobbies': ("Wandern", "Tanzen", "Skydiving"),
#                   'Eigenschaften' : {'Geschicklichkeit': 9,
#                                      'IQ': 102,






