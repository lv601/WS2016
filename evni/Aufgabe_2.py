from pprint import pprint

adressbuch = [{'vorname':'max', 'nachname':'mustermann','hobbies':('schwimmen','tanzen','lesen'), 'alter':'43',
              'eigenschaften':({'geschicklichkeit':'10', 'IQ':'98', 'gewicht':'83', 'haarfarbe':'blond'}),
              'geschlecht':'männlich'}]
adressbuch.append({'studium':'medizin'})

pprint(adressbuch[0]['eigenschaften']['IQ'])
pprint(len(adressbuch[0]['hobbies']))
pprint (len(adressbuch[0]))
pprint(adressbuch)
