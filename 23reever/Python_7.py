
# # Aufgabe 13
#
# class Entry:
#     def __init__(self, vorname, nachname, alter, geschlecht, hobbies, eigenschaften):
#         self.vorname = vorname
#         self.nachname = nachname
#         self.alter = alter
#         self.geschlecht = geschlecht
#         self.hobbies = hobbies
#         #self.hobbies.append(hobbies)
#         self.eigenschaften = hobbies
#         #self.eigenschaften.append(eigenschaften)
#
# class Adressbuch:
#     def __init__(self):
#         self.Entries = []
#
#     def add_entry(self, entry):
#         self.Entries.append(entry)
#
# ab = Adressbuch()
# entry1 = Entry("max", "muster", "42", "m", "tennis", "blond")
# ab.add_entry([entry1])
# entry2 = Entry("Hugo", "Boss", "44", "m", "kicken", "cool")
# entry3 = Entry("Kater", "Gestiefelt", "3200", "m", hobbies=["schlafen", "mulch trinken"], eigenschaften=["cute", "hungry"])
#
# ab.add_entry([entry2])
# ab.add_entry([entry3])
#
# print(entry1.__dict__)
# print(entry2.__dict__)
# print(entry3.__dict__)

# # Create class
# class Car:
#     pass
# # Create instance of class Car
# car1 = Car()
# print(car1)
#
# # Add Attributes
# car1.type = "VW W12 Roadster"
# car1.speed = 310
# print(car1.type, car1.speed)
#
# # Create another instances
# car2 = Car()
# car3 = Car()
#
# # Add Attributes
# car2.type = "Renault Ludo"
# car2.speed = 148
# car3.type = "Microcar"
# car3.speed = 49
#
# print(car1.type, car1.speed)
# print(car2.type, car2.speed)
# print(car3.type, car3.speed)
#
# class Car:
#     def __init__(self, type, speed):
#         self.type = type
#         self.speed = speed
#     string = "Ein Auto des Types {} wurde erzeugt"
#     print(string.format(self.type))
#
#     def drive(self, here, to, mode='fastest'): #self bezieht sich auf sichselbst in dem Fall "car1"
#         string = "Auto fährt von {} nach {} im Mode {}"
#         print(string.format(here, to, mode))
#     def compare(self, car2, field):
#         pass
#
# car1 = Car()
# car1.drive("A", "B")
# # Create object from class Car
# car1 = Car("Renault Ludo", 148)

# class Car:
#     def __init__(self, type, speed):
#         self.type = type
#         self.speed = speed
#
#         string = "Ein Auto des Types {} wurde erzeugt"
#         print(string.format(self.type))
#
#     def drive(self, here, to, mode='fastest'):
#         string = "Auto fährt von {} nach {} im Mode {}"
#         print(string.format(here, to, mode))
#
#     def compare(self, car2, field):
#         pass
#
# # Create object from class Car
# car1 = Car("Renault Ludo", 148)
#
# # car1 = Car()
# car1.drive("A", "B")
