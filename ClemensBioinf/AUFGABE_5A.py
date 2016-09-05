def add_person(address_book, **attributes):
    address_book.append(dict(**attributes))
    
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

add_person(Adressbuch, Vorname = "Test_Vorname", Nachname = "Test_Nachname", Hobbies = ["Hobby1", "Hobby2"], Alter = 43,
           Eigenschaften = ["Geschicklichkeit":10, "IQ": 10,"Gewicht": 10,"Haarfarbe": "blau"], Geschlecht = "weiblich")

print(Adressbuch[-1])
