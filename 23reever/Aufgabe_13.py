# Aufgabe 13

class Entry:
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.geschlecht = geschlecht
        self.hobbies = hobbies
        #self.hobbies.append(hobbies)
        self.eigenschaften = hobbies
        #self.eigenschaften.append(eigenschaften)


class Adressbuch:
    def __init__(self):
        self.Entries = []

    def add_entry(self, entry):
        self.Entries.append(entry)

ab = Adressbuch()
entry1 = Entry("max", "muster", "42", "m", "tennis", "blond")
ab.add_entry([entry1])
entry2 = Entry("Anni", "Bauer", "19", "w", "kicken", "stark")
entry3 = Entry("Kater", "Gestiefelt", "3200", "m", hobbies=["schlafen", "mulch trinken"], eigenschaften=["cute", "hungry"])

ab.add_entry([entry2])
ab.add_entry([entry3])

print(entry1.__dict__)
print(entry2.__dict__)
print(entry3.__dict__)