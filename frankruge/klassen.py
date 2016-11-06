class Car:
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

        string = "kjdsfh"
        print(string.format(self.type))

car1 = Car("Nissan quashqai", 180)