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


#class Adressbuch
        #def __init__(self)
            #self.data=[]
        #def add_entry(self, eintrag)
            #self.data.append(eintrag)





      
      
