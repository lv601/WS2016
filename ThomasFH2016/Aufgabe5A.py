from pprint import pprint

adressbuch = [{"Vorname":"Max",
               "Nachname": "Mustermann",
               "Hobbies": ["Schwimmen", "Tanzen", "Lesen"],
               "Alter": 43,
               "Eigenschaften": {"Geschicklichkeit": 10,
                                 "IQ": 98,
                                 "Gewicht": 88,
                                 "Haarfarbe": "blond"},
                "Geschlecht": "männlich"}]


def Add_Adresse(list, **adresse):
    list.append(dict(**adresse))

Add_Adresse(adressbuch, Vorname="Pia", Nachname="Musterfrau", Hobbies=["Boxen"], Alter=24,
            Eigenschaften={"Geschicklichkeit":8, "IQ":105}, Geschlecht="w")

print(len(adressbuch))
pprint(adressbuch[:-1])

