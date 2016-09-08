from pprint import pprint

adresse = {"Vorname":"Max",
           "Nachname": "Mustermann",
           "Hobbies": ["Schwimmen", "Tanzen", "Lesen"],
           "Alter": 43,
           "Eigenschaften": {"Geschicklichkeit": 10,
                             "IQ": 98,
                             "Gewicht": 88,
                             "Haarfarbe": "blond"},
           "Geschlecht": "männlich"}


adressbuch = [adresse]

#Adresse hinzufügen
adressbuch.append({"Vorname":"Pia", "Nachname":"Musterfrau", "Alter": 34, "Geschlecht":"w",
                   "Hobbies": ["Wandern", "Tanzen", "Skydiving"],
                   "Eigenschaften": {"Geschicklichkeit":9, "IQ": 102, "Gewicht:": 68, "Haarfarbe": "brünett"},
                   "Organisationen":"PyLadies"})

#Eigenschaft IQ ausgeben
print(adressbuch[0]["Eigenschaften"]["IQ"])

#Anzahl der Hobbies ausgeben (Anzahl an Listen-Elemente)
print(len(adressbuch[0]["Hobbies"]))
#Anzahl der Adressen ausgeben (Anzahl an Listen-Elemente)
print(len(adressbuch))
