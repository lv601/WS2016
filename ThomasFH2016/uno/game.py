import uuid

class game_deck():
    def __init__(self):
        self.cards = [2,5,1,9,7,12,3,6,4]

class player():
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
