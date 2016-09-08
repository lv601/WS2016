from pprint import pprint

adressbuch = [{'Vorname': 'Max', 'Nachname': 'Mustermann',
               'Hobbies': ('Schwimmen','Tanzen','Lesen'),
               'Alter': 99, 'Eigenschaften': {'Geschicklichkeit': 10, 'IQ': 55, 'Gewicht': 107, 'Haarfarbe': 'blond'},
               'Geschlecht': 'männlich'}]

adressbuch.append({'Vorname': 'Hugo', 'Nachname': 'Boss',
                'Hobbies': ('Rauchen', 'Tanzen', 'Lesen'),
                'Alter': 99, 'Eigenschaften': {'Geschicklichkeit': 1, 'IQ': 18, 'Gewicht': 88, 'Haarfarbe': 'grau'},
                'Geschlecht': 'N.A'})


def add_contact(adress_book, **kwargs):
    adress_book.append(dict(**kwargs))

add_contact(adressbuch, Vorname='Heimo', Nachname='Pfeiffenberger',
            Hobbies=('Kicken', 'Tanzen', 'Lesen'),
            Alter=93, Eigenschaften={'Geschicklichkeit': 1, 'IQ': 'nan'},
            Gewicht=108, Haarfarbe='keine')

add_contact(adressbuch, **adressbuch[0])

print(len(adressbuch))

pprint(adressbuch[-1])
