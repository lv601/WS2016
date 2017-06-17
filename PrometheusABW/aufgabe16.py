# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:38:54 2016

@author: michael
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:56:23 2016

@author: michi
"""

class EINTRAGE():
    def __init__(self):
        self.Vorname = ""
        self.Nachname = ""
        self.Hobbies = []
        self.Alter = 0
        self.Eigenschften = {}
        self.Geschlecht = ""
    
    def GetValue(self, argument):
        argument_ = self.argument
        return argument_
        
    def SetValue(self, value, argument):
        self.argument = value
    
    def AddEigenschaft(self, value, key):
        self.Eigenschaften[key] = value
    
    def AddHobbies(self, value):
        self.Hobbies.append(value)
    
    def GetAll(self):
        return  self.Vorname, self.Nachname, self.Hobbies, self.Alter, self.Eigenschften,self.Geschlecht
    
    def AddEintrag(self, **Args):
        self.Vorname = Args['Vorname']
        self.Nachname = Args['Nachname']
        self.Hobbies = Args['Hobbies']
        self.Alter = Args['Alter']
        self.Eigenschften = Args['Eigenschaften']
        self.Geschlecht = Args['Geschlecht']   


class ADRESSBUCH():
    def __init__(self):
        self.eintraege = []
    
    def __getitem__(self, value):
        return self.eintraege[value]
        
   # def SetValue(self, item, method, *Args):
   #    self.eintraege[item].method(Args[0], Args[1])
        
    def AddEntry(self, Args):
        position = EINTRAGE()
        position.AddEintrag(Args)
        self.eintraege.append(position)
    
    def Initial(self):
        position = EINTRAGE()
        self.eintraege.append(position)
    def __str__(self):
        return  "Ich heiße",self.Vorname, self.Nachname
    def __bytes__(self):
        return "No bytes here"
    def __repr__(self):
        return "Don't care"
    def __len__(self):
        return len(self.eintraege)
    def __iter__(self):
        for item in self.eintraege:
            yield item
            

Adressbuch1 = {'Vorname':'Max', 'Nachname':'Mustermann','Hobbies': ('Schwimmen','Tanzen','lesen') , 'Alter':'43' , 
'Eigenschaften':{'Geschicklichkeiten':'10' , 'IQ':'98' , 'Gewicht':'88', 'Haarfarbe': 'blond', 'Geschlecht': 'männlich'}}

Adressbuch2 = {'Vorname':'Max'}

adressen = ADRESSBUCH()
adressen.Initial()
adressen.AddEntry(Adressbuch1)
adressen.GetValue(0)
print(adressen.GetValue(0))
print(adressen.__repr__)