class Adressbuch:
    def __init__(self, Eintrag):
        self.ad=[] 
    def add_entry(self, Eintrag):
        self.ad.append(Eintrag)
    def get(self, index, key):
        return self.ad[index][key]
ab=Adressbuch({})
class Eintrag:
    def __init__(self, Vorname, Nachname, Alter, Geschlecht, Hobbies, Eigenschaften):       
        self.Vorname=Vorname
        self.Nachname=Nachname
        self.Alter=Alter
        self.Geschlecht=Geschlecht
        self.Hobbies=Hobbies
        self.Eigenschaften=Eigenschaften
        self.Eintrag=({"Vorname":self.Vorname, "Nachname":self.Nachname, "Alter":self.Alter, "Geschlecht":self.Geschlecht, "Hobbies":self.Hobbies, "Eigenschaften":self.Eigenschaften})
        
        string="{} {} wurde zum Adressbuch hinzugefügt!"
        print(string.format(self.Vorname, self.Nachname))

eintrag1=Eintrag("Stefan", "Rieger", 26, "m", ["laufen", "lachen", "lustig sein"], {"Geschicklichkeit":10})
ab.add_entry(eintrag1.Eintrag)
eintrag2=Eintrag("Max", "Mustermann", 99, "m", ["hüpfen", "humpeln", "heiter sein"], {"Geschicklichkeit":99})
ab.add_entry(eintrag2.Eintrag)
eintrag3=Eintrag("Maria", "Musterfrau", 37, "w", ["fliegen", "fluchen", "fröhlich sein"], {"Geschicklichkeit":91})
ab.add_entry(eintrag3.Eintrag)
print(ab.get(2, "Hobbies"))