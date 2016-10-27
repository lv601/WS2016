# Enthaltene Klassen: Card, UnoCard

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

class UnoCard(Card):
    def __init__(self, action):
        super().__init__(self.color, self.number)
        self.action = action


