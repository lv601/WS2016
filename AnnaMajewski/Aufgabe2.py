adr =  {"Vorname":"Max", "Nachname":"Mustermann", "Hobbies": ["Schwimmen", "Tanzen", "Lesen"], "Alter": 43, "Eigenschaften": {"Geschicklichkeit": 10, "IQ":98, "Gewicht": 88, "Haarfarbe": "blond"}, "Geschlecht": "männlich"}
zweites = {"Vorname":"Anna", "Nachname":"Majewski", "Hobbies": ["Dota", "Japanisch", "Webdesign"], "Alter": 27, "Eigenschaften": {"Geschicklichkeit": 12, "IQ":80, "Gewicht": 78, "Haarfarbe": "blond"}, "Geschlecht": "weiblich"}
print(adr)

from pprint import pprint

# pprint(adr)

buch = [adr]

print(adr["Hobbies"])

print("Der IQ beträgt", adr["Eigenschaften"]["IQ"])

print("Der IQ beträgt: ",buch[0]["Eigenschaften"]["IQ"])

count = 0
for x in adr["Hobbies"]:
    count = count + 1
print("Es gibt", count, "Hobbies.")

print("Die Länge der Liste ist:",len(buch))
print("Die Länge des Dictionary ist:",len(adr))
