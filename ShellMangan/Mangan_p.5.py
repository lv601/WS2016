Addressbuch=[{"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":["Schwimmen", "Tanzen", "Lesen"], "Alter":43, "Eigenschaften":{"Geschicklichkeit":10,"IQ":98, "Gewicht":88, "Haarfarbe":"Blond"},"Geschlecht":"Männlich"}]
def add_contact(address_book, **kwargs):
    address_book.append(dict(**kwargs))

add_contact(Addressbuch, Vorname="Pia", Nachname="Bauer", Hobbies=["Boxen"], Alter=24, Eigenschaften={"Geschicklichkeit":8, "IQ":105}, Geschlecht="m")
add_contact(Addressbuch, **Addressbuch[0])
print(Addressbuch[-1])

def get_sequence(sequence, window_size):
    for i in range(o, len(sequence)-window_size+l):
        print(" "*i, sequence[i:i+windows_size], sep= " ")

        
