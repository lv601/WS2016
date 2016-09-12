Adressbuch = [{
            "Vorname": "Max", 
            "Nachname": "Mustermann", 
            "Alter": 31, 
            "Geschlecht": "m", 
            "Hobbies": ["Lesen", "Laufen", "Lustig sein"], 
            "Eigenschaften": {"Geschicklichkeit": 3, "Stärke": 2, "Ausdauer": 9, "IQ": 3.14159265359}
            }]
            
#Zugreifen auf "Eigenschaften" "IQ"
Adressbuch[0]["Eigenschaften"]["IQ"]            

#Anzahl der Hobbies
len(Adressbuch[0]["Hobbies"])

#Adressbuch um einen ähnlichen Eintrag erweitern
Adressbuch.append({
            "Vorname": "Maria",
            "Nachname": "Musterfrau",
            "Alter": 27,
            "Geschlecht": "w",
            "Hobbies": ["Fliegen", "Fahren", "Fröhlich sein"],
            "Eigenschaften": {"Geschicklichkeit": 6, "Stärke": 1, "Ausdauer": 4, "IQ": 666}
            })
            
#Länge des Adressbuches
len(Adressbuch)