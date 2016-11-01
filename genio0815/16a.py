class Eintrag:

    def __init__(self, vorname, nachname, alter, geschlecht,
                 hobbies, eigenschaften):
        self.hobbies = []
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.geschlecht = geschlecht
        self.hobbies.append(hobbies)
        self.eigenschaften = eigenschaften

    def addHobby(self, newHobby):
        if isinstance(newHobby, str):
            self.hobbies.append(newHobby)
        else:
            print("just string like hobbies are possible")

    def listHobbies(self):
        print(*self.hobbies)

    def __str__(self):
        pp = pprint.PrettyPrinter(indent=2, width=10)
        return "Vorname: {0.vorname}\nNachname: {0.nachname}\nAlter: {0.alter}\nhobbies: {1}\n" \
               "Geschlecht: {0.geschlecht}\nEigenschaften: {2}\n".format(
                self, ",".join(self.hobbies), pp.pformat(self.eigenschaften))

    def __bytes__(self):
        return self.__str__().encode()

    def __repr__(self):
        return "Eintrag('{0.vorname}', '{0.nachname}', '{0.alter}', '{0.geschlecht}', {0.hobbies}," \
               " {0.eigenschaften})".format(self)


class Adressbuch:

    def __init__(self):
        self.entries = []

    def __init__(self, entry):
        self.entries = [*entry]

    def addEntry(self, toAdd):
        self.entries.append(toAdd)

    def getEntry(self, index):
        return self.entries[index]

    def getSize(self):
        return len(self.entries)

person1 = Eintrag('Hugo', 'Boss', 44, 'bi', 'kicken', 'cool')
person2 = Eintrag('Heinz', 'Hehenberger', 49, 'maennlich', 'frech sein', 'fad')
person1.addHobby('schlafen')
person1.addHobby('essen')

print(person1.__dict__)

ad = Adressbuch([person1, person2])

ad.addEntry(person2)

ad.getEntry(0).listHobbies()

print("adressbook got {} entries".format(ad.getSize()))

