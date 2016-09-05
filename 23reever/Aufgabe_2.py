# Dictionaries
dict = [{"Vorname": "Max", "Nachname": "Mustermann",
         "Alter": 43, "Geschlecht": "m",
        "Hobbies": ("Schwimmen", "Tanzen", "Lesen"),
        "Eigenschaften": {"Geschicklichkeit": 10,
                          "IQ":98,
                          "Gewicht":88, "Haarfarbe":"blond"}}]

#print(dict["Vorname"])
#print(dict["Eigenschaften"]["IQ"])
#print(len(dict["Hobbies"]))

from pprint import pprint
pprint(dict)

dict[0]['Eigenschaften']['IQ']
len(dict[0]['Hobbies'])

dict.append({'Vorname':"Pia", 'Nachname': "Musterfrau",
                   'Alter': 34, 'Geschlecht': "w",
                   'Hobbies': ("Wandern", "Tanzen", "Skydiving"),
                   'Eigenschaften' : {'Geschicklichkeit': 9,
                                      'IQ': 102,
                                      'Gewicht': 68,
                                      'Haarfarbe': 'brünett'},
                   'Organisationen' : 'PyLadies'})

pprint(dict)
len(dict)
