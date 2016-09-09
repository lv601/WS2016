

adressbuch = [{"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":("Schwimmen", "Tanzen", "Lesen"), "Alter":43, "Eigenschaften":{"Geschicklichkeit":10, "IQ":98, "Gewicht": 88, "Haarfarbe":"blond"}, "Geschlecht":"männlich"}]

print(len(adressbuch))


def add_contact(adressbuch, **kwargs):
    adressbuch.append(dict(**kwargs))


add_contact(adressbuch, **adressbuch[0])

add_contact(adressbuch, Vorname="Pia", Nachname="Bauer", Hobbies=["Boxen"], Alter = 24, Eigenschaften={"Geschicklichkeit": 8, "IQ":105}, Geschlecht = "m")
add_contact(adressbuch, Vorname="Asdf", Nachname="Musterfrau", Hobbies=["Boxen", "alskdjf", "asdf"], Alter=29, Eigenschaften={"Geschicklichkeit":40, "IQ":120, "Gewicht": 60, "Haarfarbe":"grün"}, Geschlecht="unklar")

print(adressbuch[-1])
print(len(adressbuch))