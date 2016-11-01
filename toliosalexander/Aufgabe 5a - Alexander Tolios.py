### Aufgabe 5a - Alexander Tolios - last modified am 06.09.2016 ; siehe Mitschrift vom 29.08.2016 ###


### Kopie von Aufgabe 2 - Alexander Tolios - last modified 06.09.2016 ; siehe Mitschrift vom 25.08.2016 ###

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

### ab hier neuer Code ###

def addab(ab, **kwargs):
    ab.append(dict(**kwargs))

addab(ab, Vorname="Maria",
    Nachname="Mustermaxi",
    Hobbies=["C", "C#", "C++"], 
    Alter=123.45,
    Geschlecht="weiblich",
    Eigenschaften={ 
        "Lesen": 14,
        "Sackhüpfen": 85.7,
#        Rechnen: 2 * int(random()+5)
        })

addab(ab, **ab[0]) # ** erzeugt ein dictionary, dictionaries werden auch durch ** entpackt
ab[-1]

ab        
        