Adressbuch = [{'Vorname':"Max", 'Nachname': "Mustermann", 'Alter': 43, 'Hobbies': ("Schwimmen", "Tanzen", "Lesen"),
'Eigenschaften' : {'Geschicklichkeit': 10, 'IQ': 98, 'Gewicht': 88, 'Haarfarbe': 'blond'}, 'Geschlecht': "männlich"}]


from pprint import pprint
pprint(Adressbuch)





print(Adressbuch[0]['Eigenschaften']['IQ'])


len (Adressbuch[0]['Hobbies'])
print(Adressbuch[0]['Hobbies'])
print(Adressbuch[0]['Hobbies'][1])


len(Adressbuch)
len(Adressbuch[0])



Adressbuch[0]['Eigenschaften']['Größe'] = '1.75m'
Adressbuch[0]['Eigenschaften']['Haarfarbe'] = 'braun'
Adressbuch[0]['zweiterVorname'] = 'Domenik'



from pprint import pprint
pprint(Adressbuch)