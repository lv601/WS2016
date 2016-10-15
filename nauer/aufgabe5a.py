#!/usr/bin/env python3

""" Aufgabe 5a
Erstellen Sie eine Funktion um dem Dictionary von Aufgabe 2 weite Datensätze hinzuzufügen
"""

from pprint import pprint

# Define function
def add_contact(address_book, **kwargs):
    address_book.append(dict(**kwargs))

Adressbuch = []

# Use key value pairs
add_contact(Adressbuch, Vorname="Pia", Nachname="Bauer",
    Hobbies=["Boxen"], Alter=24,
    Eigenschaften={'Gechicklichkeit': 8, 'IQ': 105},
    Geschlecht='m')

# Unpack dictionary
add_contact(Adressbuch, **Adressbuch[0])

# Show last entry
pprint(Adressbuch[-1])
pprint(Adressbuch)

