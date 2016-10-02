from pprint import pprint

# Funktion Datensätze zu Dict hinzufügen
# ** erlaubt übergabe von mehreren keyworded argmuments
def add_contact(address_book, **new_contact):
    address_book.append(dict(**new_contact))

adress_book = []

# Aufruf der Funktion "key value pairs"
add_contact(adress_book, Vorname="Pia", Nachname="Bauer",
    Hobbies=["Boxen"], Alter=24,
    Eigenschaften={'Gechicklichkeit': 8, 'IQ': 105},
    Geschlecht='m')

#pprint(adress_book)

add_contact(adress_book, Vorname="Peter", Nachname="Huber",
            Hobbier=["Computerspiele"], Alter=46,
            Eigenschaften={'Geschicklichkeit': 12, 'IQ': 108},
            Geschlecht='f')

# pprint(adress_book)

# Unpack dictionary
# add_contact(adress_book, **adress_book[0])

# Show last entry -> Zugriff in python auch ohne len() möglich
pprint(adress_book[-1])
# pprint(adress_book)
