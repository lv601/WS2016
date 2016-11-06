class entry: # Eine Klasse entry wird erstellt
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname=vorname
        self.nachname=nachname
        self.alter=alter
        self.geschlecht=geschlecht
        self.hobbies=hobbies
        self.eigenschaften=eigenschaften

    def __str__(self):
        return "Der Name des Benutzers ist " + self.vorname + " " + self.nachname

    def __bytes__(self):
        return b"Byte time" 

    def __repr__(self):
        return "Der Name des Benutzers ist " + self.vorname + " " + self.nachname

class Adresses: 
    def __init__(self):
        self.data =[]

    def __getitem__(self, item):
        return self.data[item] 

    def __iter__(self):
        for entry in self.data: 
            yield entry

    def __len__(self):
        return len(self.data) 

    def add_entry(self, entry): 
        self.data.append(entry)

    def get_entry(self, index):
        return self.data[index]


adressen = Addresses()
data = [{'vorname': "Max", 'nachname': "Mustermann",'alter': 43, 'geschlecht': "m",'hobbies': ("Schwimmen", "Tanzen", "Lesen"),'eigenschaften': {'Geschicklichkeit': 10,'IQ': 98,'Gewicht': 88,'Haarfarbe': 'blond'}},{'vorname': "Pia", 'nachname': "Musterfrau",'alter': 34, 'geschlecht': "w",'hobbies': ("Wandern", "Tanzen", "Skydiving"),'eigenschaften': {'Geschicklichkeit': 9,'IQ': 102,'Gewicht': 68,'Haarfarbe': 'br�nett'}}]

Addresses.add_entry(entry(**data[0]))
Addresses.add_entry(entry(**data[1]))
print(Addresses.entry[0])
print(bytes(Addresses.entry[0]))
print(repr(Addresses.entry[0]))
print(eval(repr(Addresses.entry[0])))