class Car:
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        string = "Ein Auto des Types {} wurde erzeugt"
        print(string.format(self.type))

# Create object from class Car
car1 = Car("Renault Ludo", 148)