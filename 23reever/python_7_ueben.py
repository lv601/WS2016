class car:
    pass

car1 = car()
print(car1)

car1.types = "VW"
car1.speed = 310
print(car1.speed, car1.types)

class Car:
    def drive(selfself, here, to, mode="fastest"):
        string = "Auto fährt von {} nach {} im MOde{}"
        print(string.format(here, to, mode))

car1 = Car()
car1.drive(here="A", to="B")

class A:
    def __init__(self, val):
        self.attribute_1 = val
        self.atrribute_2 = "Test"

a = A([1, 2, "!"])

print(a.attribute_1, a.atrribute_2)

a.welt = "Hello World"
a.__dict__["zahl"] = 100

print(a.__dict__)