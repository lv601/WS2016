class Eintrag:
    def __init__(self, vorname, nachname, alter, geschlecht,
                hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.hobbies = hobbies
        self.geschlecht = geschlecht
        self.eigenschaften = eigenschaften

class Adressbuch:
    def __init__(self):
        self.data = []

    def add_entry(self, eintrag):
        self.data.append(eintrag)

    def get_entry(self, index):
        return self.data[index]

eintrag1 = Eintrag("Maria", "Hinterhuber", "102", "x", "Geige, PingPong, Männer", "alt") # einfach in die klammer wie oben verlangt vorname, nachname, alter etc....

ab1 = Adressbuch()

ab1.add_entry(eintrag1)
show_entry = ab1.get_entry(0)
print (show_entry.__dict__)