#Bsp 13

#adrs=[{"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":"Schwimmen, Tanzen, Lesen", "Alter":43, "Eigenschaften":{"Geschicklichkeit":10,"IQ":98, "Gewicht":88, "Haarfarbe":"Blond"},"Geschlecht":"Männlich"}]
#adr={"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":["Schwimmen", "Tanzen", "Lesen"], "Alter":43, "Eigenschaften":{"Geschicklichkeit":10,"IQ":98, "Gewicht":88, "Haarfarbe":"Blond"},"Geschlecht":"Männlich"}
#print(adr)
#from pprint import pprint
#pprint(adr)
#print(adr["Hobbies"])
#print(adr["Eigenschaften"]["IQ"])
#print(adrs[0]["Hobbies"])
#hobbies=0
#for x in adr["Hobbies"]:
#    hobbies=hobbies+1
#print("He has", hobbies, "Hobbies")
#print(len(adr))

class Addresses:
    def __init__(self):
        self.entries=[]
    def add_entry(self, entry):
        self.entries.append(entry)

class entry:
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname=vorname
        self.nachname=nachname
        self.alter=alter
        self.geschlecht=geschlecht
        self.hobbies=hobbies
        self.eigenschaften=eigenschaften

adressen = Addresses()


data = [{'vorname': "Max", 'nachname': "Mustermann",'alter': 43, 'geschlecht': "m",'hobbies': ("Schwimmen", "Tanzen", "Lesen"),'eigenschaften': {'Geschicklichkeit': 10,'IQ': 98,'Gewicht': 88,'Haarfarbe': 'blond'}},
        {'vorname': "Pia", 'nachname': "Musterfrau",'alter': 34, 'geschlecht': "w",'hobbies': ("Wandern", "Tanzen", "Skydiving"),'eigenschaften': {'Geschicklichkeit': 9,'IQ': 102,'Gewicht': 68,'Haarfarbe': 'brünett'}}]

adressen.add_entry(entry(**data[0]))
adressen.add_entry(entry(**data[1]))






      
      
