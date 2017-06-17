# Aufgabe 16

class Entry:
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.geschlecht = geschlecht
        self.hobbies = hobbies
        #self.hobbies.append(hobbies)
        # Achtung: hobbies und eigenschaften ist bereits eine liste oder dict
        self.hobbies = hobbies
        self.eigenschaften = eigenschaften
        #self.eigenschaften.append(eigenschaften)
    def __repr__(self):
        # Achtung: see https://docs.python.org/3/library/functions.html#repr
        return "Entry('{0.vorname}', '{0.nachname}', {0.alter}, '{0.geschlecht}', {0.hobbies}, {0.eigenschaften})".format(self)
        #return "Entry()"
    def __str__(self):
        return "Das ist ein Eintrag"
    def __bytes__(self):
        return b"Das ist ein Eintrag"

class Adressbuch:
    def __init__(self):
        self.Entries = []

    def add_entry(self, entry):
        self.Entries.append(entry)

    def __getitem__(self, item):
        return self.Entries

    def __iter__(self):
        for item in self.Entries:
            yield item

    def __len__(self):
        return len(self.Entries)


# INFO: Verwende diese Klausel in Bibliotheken. Dann braucht man sie nicht wegkommentieren
if __name__ == "__main__":
    ab = Adressbuch()
    print(str(ab))
    entry1 = Entry("max", "muster", "42", "m", ["tennis", "lesen"], {'Haarfarbe':"blond", 'Geschicklichkeit':8})
    ab.add_entry([entry1])
    entry2 = Entry("Anni", "Bauer", "19", "w", "kicken", "stark")
    entry3 = Entry("Kater", "Gestiefelt", "3200", "m", hobbies=["schlafen", "mulch trinken"], eigenschaften=["cute", "hungry"])

    ab.add_entry([entry2])
    ab.add_entry([entry3])

    print(entry1.__dict__)
    print(entry2.__dict__)
    print(entry3.__dict__)

    # INFO: repr mit eval kann neues Objekt erzeugen
    print(repr(entry1))
    entry4 = eval(repr(entry1))
