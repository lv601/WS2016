from pprint import pprint
def add_contact(address_book, **kwargs):
    address_book.append(dict(**kwargs))

Adressbuch = []

add_contact(Adressbuch, Vorname="Pia", Nachname="Musterfrau",
    Hobbies=["Wandern", "Tanzen", "Skydiving"], Alter=34,
    Eigenschaften= ["Gechicklichkeit:9", "IQ:102", "Gewicht:68", "Haarfarbe : bruenett"],
    Geschlecht= "w")

add_contact(Adressbuch, **Adressbuch[0])

#pprint(Adressbuch)
pprint(Adressbuch[-1])