import random

class StandardCard:

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return str(self.color)+" "+str(self.value)
    def __print__(self):
        print(str(self))


class cardDeck:
    def __init__(self):
        self.deck=[]
    def generate_deck(self):
        self.deck=[]
        for value in range(1,10):
            for color in ["red", "blue", "green", "yellow"]:
                self.deck.append(str(StandardCard(color, value)))

        return self.deck
    def __str__(self):
        return self.deck

A=cardDeck()
print(A)
number_players = 3
a=StandardCard("red", 2)
print(a)