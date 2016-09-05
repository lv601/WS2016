from pprint import pprint

adressbuch = [{'Vorname': 'Max', 'Nachname': 'Mustermann',
               'Hobbies': ('Schwimmen','Tanzen','Lesen'),
               'Alter': 99, 'Eigenschaften': {'Geschicklichkeit': 10, 'IQ': 55, 'Gewicht': 107, 'Haarfarbe': 'blond'},
               'Geschlecht': 'männlich'}]

print(adressbuch[0]['Eigenschaften']['IQ'])
print(len(adressbuch[0]['Hobbies']))

adressbuch.append({"Vorname": "Hugo", "Nachname": "Boss",
                "Hobbies": ("Rauchen", "Tanzen", "Lesen"),
                "Alter": 99, "Eigenschaften": {"Geschicklichkeit": 1, "IQ": 18, "Gewicht": 88, "Haarfarbe": "grau"},
                "Geschlecht": "N.A"})

print(len(adressbuch))

pprint(adressbuch)