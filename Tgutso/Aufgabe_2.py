from pprint import pprint

Adressbuch = [{"Vorname":"Max", "Nachname":"Mustermann", "Alter": 43, "Geschlecht": "männlich", "Hobbies": ("Schwimmen", "Tanzen", "Lesen"), "Eigenschaften": {"Geschicklichkeit": 10, "IQ": 98, "Gewicht": 88, "Haarfarbe": "blond"}}]

pprint(Adressbuch[0]["Eigenschaften"]["IQ"])
pprint(len(Adressbuch[0]["Hobbies"]))

Adressbuch.append({"Vorname":"Tamas", "Nachname":"Gutsohn", "Alter": 31, "Geschlecht": "männlich", "Hobbies": ("Schwimmen", "Fliegen", "Reisen"), "Eigenschaften": {"Geschicklichkeit": 100, "IQ": 198, "Gewicht": 78, "Haarfarbe": "braun"}})

pprint(Adressbuch)

pprint(len(Adressbuch))