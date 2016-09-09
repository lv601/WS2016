def add_contact(Adressbuch, **kwargs):
    Adressbuch.append(dict(**kwargs))
    
Adressbuch = [{
            "Vorname": "Max", 
            "Nachname": "Mustermann", 
            "Alter": 31, 
            "Geschlecht": "m", 
            "Hobbies": ["Lesen", "Laufen", "Lustig sein"], 
            "Eigenschaften": {"Geschicklichkeit": 3, "Stärke": 2, "Ausdauer": 9, "IQ": 3.14159265359}
            }]
            
add_contact(Adressbuch, Vorname = "Stefan", 
            Nachname = "Rieger",
            Alter= 26,
            Hobbies=["Einführung in das Programmieren", "Statistik", "Ausgewählte Kapite der Mathematik"],
            Geschlecht= "m",
            Eigenschaften= {"Toll sein": 500, "Programmieren": -8})
            
#letzten Entry abfragen:
Adressbuch[-1]