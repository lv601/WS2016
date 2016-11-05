# Included classes: Card, Card_Uno

class Card:
    def __init__(self, color, symbol, action):
        self.color = color
        self.symbol = symbol
        self.action = action

# Card_Uno notwendig?
class Card_Uno(Card):
    def __init__(self, color, number, action):
        Card.__init__(self, color, number, action)


# TestCard = Card_Uno('red',1, 'skip')
# print(TestCard.color, TestCard.symbol, TestCard.action)
