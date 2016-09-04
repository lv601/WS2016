## Date: 04.09.2016
## Author: Anna Majewski
## Description: Aufgabe 2
## Zuerst ein Dictionary erstellen, Sachen mit Indizes herauslesen, dann zusätzlichen Eintrag speichern.

from pprint import pprint
# damit Sachen schick angezeigt werden

buch = {"Vorname":"Max",
         "Nachname": "Mustermann",
         "Hobbies": ["Schwimmen", "Tanzen", "Lesen"],
# Hobbies wird als Liste eingefügt, da es nicht immer gleich viele Felder haben wird.
         "Alter": 43,
         "Eigenschaften":
# Eigenschaften ist ein eigenes dictionary.
            {"Geschicklichkeit": 10,
             "IQ": 98,
             "Gewicht": 88,
             "Haarfarbe": "blond"},
        "Geschlecht": "männlich"}

## Wrap it up in a list
addressbuch = [buch]
pprint(addressbuch), auskommentiert weil ich in aufgabe5.py diese Datei importiere

## Zusätzliche Aufgaben:
# Geben Sie den IQ aus.

print("Der IQ beträgt:", addressbuch[0]["Eigenschaften"]["IQ"])

# Geben Sie die Anzahl der Hobbies aus

count = 0
for x in addressbuch[0]["Hobbies"]:
    count += 1
print("Die Anzahl der Hobbies ist:", count)

# Fügen Sie einen ähnlichen Datensatz hinzu.
# Da es eine Liste ist, kann man mit .append einen Eintrag hinzufügen.

addressbuch.append({"Vorname": "Taka", "Nachname": "Baka", "Hobbies": ["Games", "Webdesign"], "Eigenschaften": {"Haarfarbe": "braun"},"Geschlecht": "weiblich"})

# Zeigen Sie die Länge des Addressbuchs an

length = len(addressbuch)
print ("Die Länge des Addressbuchs ist:", length)
