class mydict(dict):
    """
    Erweitere die Dictionary Klasse um weitere
    Funktionalität
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("My superdict;", list(kwargs))

    def get_list_of_keys(self):
        return list(self.keys())

d = mydict(a="a", b="b")
print(d.get_list_of_keys())


class mydata:
    def __init__(self, identity, **kwargs):
        self.__dict__.update(kwargs)
        self.id = identity

d = {'x': 5, 'y': 10, 'z': -3}

data = mydata("afg23", **d)

print(data.id, data.x, data.y, data.z)


import math

class GeoPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)

class CircleShape(GeoPoint):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
        self.area = math.pi * self.r ** 2
        self.circumference = math.pi * self.r * 2

class RectShape(GeoPoint):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.width = w
        self.height = h

    def get_corners(self):
        return ((self.x, self.y), (self.x, self.y + self.width),
                (self.x + self.height, self.y), (self.x + self.height, self.y + self.width))

rect = RectShape(4,4,10,15)
print(rect.get_pos())
print(rect.get_corners())