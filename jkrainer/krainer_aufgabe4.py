

adressbuch = [{"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":("Schwimmen", "Tanzen", "Lesen"), "Alter":43, "Eigenschaften":{"Geschicklichkeit":10, "IQ":98, "Gewicht": 88, "Haarfarbe":"blond"}, "Geschlecht":"männlich"}]

print(len(adressbuch))

#adressbuch[0]["Eigenschaften"]["IQ"]

#len(adressbuch[0]["Hobbies"])

#neu_eintrag = [{"Vorname":"Asdf", "Nachname":"Musterfrau", "Hobbies":("Boxen", "alskdjf", "asdf"), "Alter":29, "Eigenschaften":{"Geschicklichkeit":40, "IQ":120, "Gewicht": 60, "Haarfarbe":"grün"}, "Geschlecht":"unklar"}]

#adressbuch.append(neu_eintrag)

#len(adressbuch)
def add_contact(adress_book, **kwargs):
    adress_book.append(dict(**kwargs))

add_contact(adressbuch, Vorname="Pia", Nachname="Bauer", Hobbies=["Boxen"], Alter = 24, Eigenschaften={"Geschicklichkeit": 8, "IQ":105}, Geschlecht = "m")

add_contact(adressbuch, **adressbuch[0])

print(adressbuch[-1])