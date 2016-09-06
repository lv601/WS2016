### Aufgabe 2 - Alexander Tolios - last modified 06.09.2016 ; siehe Mitschrift vom 25.08.2016 ###

ab = [{
    "Vorname": "Max",
    "Nachname": "Mustermann",
    "Hobbies": ["R", "Python"], 
    "Alter": 25.9,
    "Geschlecht": "männlich",
    "Eigenschaften": { 
        "Lesen": 24,
        "Schreiben": 25.3,
#        Rechnen: 2 * int(random()+5
        }
        }]


ab[0].keys() # -> Weil 1st Element der Liste (Element Nr. 1)
ab[0]["Alter"]
ab[0]["Eigenschaften"]["Lesen"]
print("Max Mustermanns Alter ist: ", ab[0]["Alter"])
len(ab[0])
len(ab[0]["Hobbies"])



ab2 = [{
    "Vorname": "Maria",
    "Nachname": "Mustermaxi",
    "Hobbies": ["C", "C#", "C++"], 
    "Alter": 123.45,
    "Geschlecht": "weiblich",
    "Eigenschaften": { 
        "Lesen": 14,
        "Sackhüpfen": 85.7,
#        Rechnen: 2 * int(random()+5
        }
        }]

ab = ab + ab2
len(ab)

# CAVE: funktioniert nur einmal, sonst wird immer ein neues identisches ab2 hinten angehängt!

# bessere Version mit append:

ab.append({
    "Vorname": "Maria",
    "Nachname": "Mustermaxi",
    "Hobbies": ["C", "C#", "C++"], 
    "Alter": 123.45,
    "Geschlecht": "weiblich",
    "Eigenschaften": { 
        "Lesen": 14,
        "Sackhüpfen": 85.7,
#        Rechnen: 2 * int(random()+5
        }
        })

len(ab)

# CAVE: funktioniert nur einmal, sonst wird immer ein neues identisches ab hinten angehängt!


pprint(ab) # Magic functioni; aktiviert hübscheres printing (Zeilenschreibweise werden in der Konsole ausgegeben)
