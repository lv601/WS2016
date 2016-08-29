#aufgabe 2
#erstelle ein dictionary einer Personenkartei
"""
Adressbuch:
Vorname:Max
Nachname:Mustermann
Hobbies: Schwimmen,Tanzen,lesen
Alter:43
Eigenschaften:
    Geschicklichkeiten:10
    IQ:98
    Gewicht:88
    Haarfarbe: blond
    Geschlecht männlich
"""

Adressbuch = {'Vorname':'Max', 'Nachname':'Mustermann','Hobbies': ('Schwimmen','Tanzen','lesen') , 'Alter':'43' , 
'Eigenschaften':{'Geschicklichkeiten':'10' , 'IQ':'98' , 'Gewicht':'88', 'Haarfarbe': 'blond', 'Geschlecht': 'männlich'}}

from pprint import pprint
#pprint(Adressbuch)
eigenschaften = Adressbuch['Eigenschaften']
print(eigenschaften['IQ'])
 
print(len(Adressbuch['Hobbies']))
#addiere aehnlichen datensatz
#zeige länge des adressbuches