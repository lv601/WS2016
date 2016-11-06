class Adresse:
    def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.hobbies = hobbies
        self.geschlecht = geschlecht
        self.eigenschaften = eigenschaften

    def __str__(self):
        return "Vorname: {0.vorname}\nNachname: {0.nachname}\nAlter: {0.alter}\nHobbies: {1}\nGeschlecht: {0.geschlecht}\nEigenschaften: {2}\n".format(
            self, ",".join(self.hobbies), self.eigenschaften)

    def __bytes__(self):
        return self.__str__().encode()

    def __repr__(self):
        return "Adresse('{0.vorname}', '{0.nachname}', '{0.alter}', '{0.geschlecht}', {0.hobbies}, {0.eigenschaften})".format(self)


class Adressbuch:
    def __init__(self):
        self.Adressen = []

    def Add_Adresse(self, Adresse):
        self.Adressen.append(Adresse)

adressen = Adressbuch()
