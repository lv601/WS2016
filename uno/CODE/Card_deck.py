# Included classes: Deck
from Cards import Card

class Deck:
    def __init__(self, deck = []):
        self.deck = deck

class Deck_Uno(Deck):
    def __init__(self, deck = []):
        Deck.__init__(self, deck)

    def create_deck(self):
        colors = ['red','yellow','green','blue']
        for color in colors:
            for symbol in range(1, 10):
                # 1 - 9
                new_card = Card(color, symbol, action=None)
                self.deck.append(new_card)
                new_card = Card(color, symbol, action=None)
                self.deck.append(new_card)
                # 0
            new_card = Card(color, 0, action=None)
            self.deck.append(new_card)
            # Draw 2
            new_card = Card(color, None, action="draw2")
            self.deck.append(new_card)
            new_card = Card(color, None, action="draw2")
            self.deck.append(new_card)
            # Reverse
            new_card = Card(color, None, action="reverse")
            self.deck.append(new_card)
            new_card = Card(color, None, action="reverse")
            self.deck.append(new_card)
            # Skip
            new_card = Card(color, None, action="skip")
            self.deck.append(new_card)
            new_card = Card(color, None, action="skip")
            self.deck.append(new_card)
            # Wildcards
            new_card = Card(None, None, action="wildcard")
            self.deck.append(new_card)
            new_card = Card(None, None, action="wildcard4")
            self.deck.append(new_card)

        return self.deck

myDeck = Deck_Uno()
myDeck.create_deck()


# for element in myDeck.deck:
#      print(element.color, element.symbol, element.action)
# print(len(myDeck.deck))


        # Total: 25 of each color + 4 wild cards + 4 wild draw 4 cards
        # 2 Draw Two
        # 2 Reverse
        # 2 Skip
        # 2 of each Number 1-9
        # 1 of Number 0
