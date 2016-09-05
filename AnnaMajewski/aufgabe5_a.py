## Date: 04.09.2016
## Author: Anna Majewski
## Description: Funktionen um bereits erstellte Programme erstellen

# Aufgabe 2: Erstellen Sie eine Funktion um dem Dictionary
# von Aufgabe 2 weitere Datensätze hinzuzufügen

from pprint import pprint

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

def neu_buch(book, **kwargs):
    addressbuch.append(dict(**kwargs))
# neu_buch ist eine Funktion, die man zum Hinzufügen von Einträgen nutzen kann
# **kwargs = keywordarguments, die man eingeben kann.

# Zum Befüllen kann man die vorher definierten Keys nutzen.
neu_buch(addressbuch, Name = "Maxine", Nachname = "Musterfrau", Hobbies = ["Singen", "Tanzen", "Springen"], Eigenschaften = {"IQ": 200, "Geschicklichkeit": 200, "Geduld": 10}, Geschlecht= "weiblich")

pprint(addressbuch[0:])
# alle Einträge ausgegeben.
