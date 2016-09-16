Addressbuch=[{"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":["Schwimmen", "Tanzen", "Lesen"], "Alter":43, "Eigenschaften":{"Geschicklichkeit":10,"IQ":98, "Gewicht":88, "Haarfarbe":"Blond"},"Geschlecht":"Männlich"}]
def add_contact(address_book, **kwargs):
    address_book.append(dict(**kwargs))

add_contact(Addressbuch, Vorname="Pia", Nachname="Bauer", Hobbies=["Boxen"], Alter=24, Eigenschaften={"Geschicklichkeit":8, "IQ":105}, Geschlecht="m")
add_contact(Addressbuch, **Addressbuch[0])
print(Addressbuch[-1])

# ACHTUNG da waren ein paar Typos drin
def get_sequence(sequence, window_size):
    for i in range(0, len(sequence) - window_size + 1):
        print(" "*i, sequence[i:i+window_size], sep=" ")

get_sequence("ABCDEFGHIJ", 4)
