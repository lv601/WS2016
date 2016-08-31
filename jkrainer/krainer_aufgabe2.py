adressbuch = [{"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":("Schwimmen", "Tanzen", "Lesen"), "Alter":43, "Eigenschaften":{"Geschicklichkeit":10, "IQ":98, "Gewicht": 88, "Haarfarbe":"blond"}, "Geschlecht":"männlich"}]

print(adressbuch[0]["Eigenschaften"]["IQ"])

print(len(adressbuch[0]["Hobbies"]))

neu_eintrag = [{"Vorname":"Asdf", "Nachname":"Musterfrau", "Hobbies":("Boxen", "alskdjf", "asdf"), "Alter":29, "Eigenschaften":{"Geschicklichkeit":40, "IQ":120, "Gewicht": 60, "Haarfarbe":"grün"}, "Geschlecht":"unklar"}]

adressbuch.append(neu_eintrag)

print(len(adressbuch))
