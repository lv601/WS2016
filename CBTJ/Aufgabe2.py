adressbuch = [{'Vorname':'Max', 'Nachname':'Mustermann', 'Hobbies': ('Schwimmen','Tanzen','Lesen'), 'Alter': 43,
               'Eigenschaften' : {'Geschicklichkeit': 10, 'IQ':98, 'Gewicht':88, 'Haarfarbe':'blond'},'Geschlecht':'männlich'}]

IQ = adressbuch [0] ['Eigenschaften'] ['IQ']

print (IQ)


number_hobbies = len(adressbuch  [0] ['Hobbies'])

print (number_hobbies)

adressbuch.append ({'Vorname':'Pia', 'Nachname': 'Musterfrau', 'Alter': 34, 'Geschlecht': 'w', 'Hobbies': ('Wandern', 'Tanzen', 'Skydiving'),
                   'Eigenschaften': {'Geschicklichkeit' : 9, 'IQ' : 102, 'Gewicht' : 68, 'Haarfarbe' : 'brünett'}, 'Organisationen' : 'PyLadies'})

length_adress= len(adressbuch)

print (length_adress)