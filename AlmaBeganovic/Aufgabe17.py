class data:
    def __init__(self, Vorname, Nachname, Hobbies, Alter, Eigenschaften, Geschlecht):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Hobbies=Hobbies
        self.Alter=Alter
        self.Eigenschaften=Eigenschaften
        self.Geschlecht=Geschlecht

    # ACHTUNG: Einrückungsfehler
    def __repr__(self):
        # Achtung: see https://docs.python.org/3/library/functions.html#repr
        return "data('{0.Vorname}', '{0.Nachname}', {0.Hobbies}, {0.Alter}, {0.Eigenschaften},'{0.Geschlecht}')".format(self)
    #def __repr__(self):
    #    return "data()"

    # TIPP: Hier wäre eine repräsentierbarere Ausgabe mehr Sinnvoll. zB. eine formatierte Ausgabe des Inhaltes
    def __str__(self):
        return "Ich bin vom Typ data "


    def __bytes__(self):
        return b"Ich bin vom Typ data"

class Adressbuch:
    def __init__(self):
        self.data = []

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        # Achtung: Typo
        for i in self.data:
            #yield item
            yield i
data('Max', 'Mustermann', ['Schwimmen', 'Tanzen', 'Lesen'], 45, {'Haarfarbe': 'blond'}, 'männlich')
    def __len__(self):
        return len(self.data)


    def add_entry(self, data):
        self.data.append(data)

# INFO: Verwende diese Klausel in Bibliotheken. Dann braucht man sie nicht wegkommentieren
if __name__ == "__main__":
    #test = data("Max", "Mustermann", "Schwimmen,Tanzen und Lesen", 45, "Haarfarbe:blond", "männlich")

    # TIPP: Für Eigenschaften eignet sich hier eine Liste besser und für Eigenschaften ein dict
    test = data("Max", "Mustermann", ["Schwimmen", "Tanzen", "Lesen"], 45, {'Haarfarbe': "blond"}, "männlich")

    print(test.Alter, test.Nachname)

    ad = Adressbuch()
    ad.add_entry(test)

    # ACHTUNG: Sie überschreiben hier die Klasse data mit einer Instanz. Danach können Sie keine neue Instanz mit data()
    # erstellen.
    # for data in ad:
    #     print(data)
    for entry in ad:
        print(entry)


    print(len(ad))
    print(ad)

    #for item in ad:
        #print (item)

    # INFO: repr mit eval kann neues Objekt erzeugen
    print(repr(test))

    test2 = eval(repr(test))
    print(test2)


