Adressbuch = [{
    "Vorname": "Max",
    "Nachname": "Mustermann",
    "Hobbies": ["Schwimmen", "Tanzen", "Lesen"],
    "Alter": 43,
    "Eigenschaften": {
        "Geschicklichkeit": 10,
        "IQ": 98,
        "Gewicht": 88,
        "Haarfarbe": "blond"
        },
    "Geschlecht": "maennlich"
    }]

print("IQ:", Adressbuch[0]["Eigenschaften"]["IQ"])
print("Anzahl Hobbies:", len(Adressbuch[0]["Hobbies"]))

Adressbuch.append({
    "Vorname": "Tim",
    "Nachname": "Timbo",
    "Hobbies": ["Fallschirmspringen", "Basketball", "Programmieren"],
    "Alter": 92,
    "Eigenschaften": {
        "Geschicklichkeit": 1,
        "IQ": 100,
        "Gewicht": 70,
        "Haarfarbe": "blau"
        },
    "Geschlecht": "maennlich"
    })

print("Laenge Adressbuch:", len(Adressbuch))