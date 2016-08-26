
adrs=[{"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":"Schwimmen, Tanzen, Lesen", "Alter":43, "Eigenschaften":{"Geschicklichkeit":10,"IQ":98, "Gewicht":88, "Haarfarbe":"Blond"},"Geschlecht":"Männlich"}]
adr={"Vorname":"Max", "Nachname":"Mustermann", "Hobbies":["Schwimmen", "Tanzen", "Lesen"], "Alter":43, "Eigenschaften":{"Geschicklichkeit":10,"IQ":98, "Gewicht":88, "Haarfarbe":"Blond"},"Geschlecht":"Männlich"}
print(adr)
from pprint import pprint
pprint(adr)
print(adr["Hobbies"])
print(adr["Eigenschaften"]["IQ"])
print(adrs[0]["Hobbies"])
hobbies=0
for x in adr["Hobbies"]:
    hobbies=hobbies+1
print("He has", hobbies, "Hobbies")
print(len(adr))
      
      
