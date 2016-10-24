Adressbuch = []


def add_contact(address_book, **kwargs):
	address_book.append(dict(**kwargs))

	
add_contact(Adressbuch, Vorname = "sofia", Nachname = "kugler", Alter= 4, Hobbies = ["Schwimmen", "Lesen"],
Eigenschaften = {'Geschicklichkeit':10, 'Gewicht':15, 'Haarfarbe':'blond'}, Geschlecht="w")

add_contact(Adressbuch, Vorname="Max", Nachname= "Mustermann", Alter= 6, Hobbies= ["Schwimmen", "Tanzen", "Lesen"],
Eigenschaften = {'Geschicklichkeit': 10, 'Gewicht': 17, 'Haarfarbe': 'braun'}, Geschlecht = "m")

from pprint import pprint
pprint(Adressbuch)


