# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 20:54:12 2016

@author: lv
"""


def add_contact(address_book, **kwargs):
    address_book.append(dict(**kwargs))
    
Adressbuch=[]   

add_contact(Adressbuch, Vorname="Bia", Nachname="Pauer",
            Hobbies=["Boxen"], Alter=24,
            Eigenschaften={'Geschicklichkeit ':8, 'IQ ': 105},
            Geschlecht='m')
            
add_contact(Adressbuch, **Adressbuch[0])

Adressbuch[-1]


