from pprint import pprint

def eintragen (bestehend, neu):
    dn=dict(neu)
    bestehend.append(dn)


adressbuch = [{'Vorname':'Max', 'Nachname':'Mustermann', 'Hobbies': ('Schwimmen','Tanzen','Lesen'), 'Alter': 43,
               'Eigenschaften' : {'Geschicklichkeit': 10, 'IQ':98, 'Gewicht':88, 'Haarfarbe':'blond'},'Geschlecht':'männlich'}]


adressbuch.append ({'Vorname':'Pia', 'Nachname': 'Musterfrau', 'Alter': 34, 'Geschlecht': 'w', 'Hobbies': ('Wandern', 'Tanzen', 'Skydiving'),
                   'Eigenschaften': {'Geschicklichkeit' : 9, 'IQ' : 102, 'Gewicht' : 68, 'Haarfarbe' : 'brünett'}, 'Organisationen' : 'PyLadies'})


newdata = [('Vorname', 'Johann'), ('Nachname', 'Wendelin'), ('Hobbies', ('Funken','Fischen','Flugzeuge')), ('Alter', '55'),
            ('Eigenschaften', dict((('Geschicklichkeit', '70'), ('IQ', '3'),('Gewicht', '150'), ('Haarfarbe', 'grau')))), ('Geschlecht', 'x')]

eintragen (adressbuch, newdata)

pprint (adressbuch)