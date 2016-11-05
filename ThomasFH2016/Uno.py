import random

class StandardCard:

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def as_string(self):
        return self.color + " " + str(self.value)

class ActionCard:

    REVERSE = 'Reverse'
    SKIP = 'Skip'
    DRAW2 = 'Draw 2'

    def __init__(self, color, action):
        self.action = action
        self.color = color

    def as_string(self):
        return self.color + " " + self.action

class WildCard:

    WILD = 'Wild'
    WILD4 = 'Wild + 4'

    def __init__(self, action):
        self.action = action

    def as_string(self):
        return self.action


class CardDeck:

    def __init__(self):
        self.cards = []
        self.CreateDeck()
        self.Shuffle()
        self.staple = []
        #self.cards.append(self.CreateDeck())

    def CreateDeck(self):
        for i in range(10):
            for color in ['Blue', 'Green', 'Red', 'Yellow']:
                self.cards.append(StandardCard(color, i))
        for i in range(2):
            for color in ['Blue', 'Green', 'Red', 'Yellow']:
                self.cards.append(ActionCard(color, ActionCard.REVERSE))
                self.cards.append(ActionCard(color, ActionCard.SKIP))
                self.cards.append(ActionCard(color, ActionCard.DRAW2))
        for i in range(4):
            self.cards.append(WildCard(WildCard.WILD))
            self.cards.append(WildCard(WildCard.WILD4))

    def draw_card(self):
        card = self.cards.pop()
        return card

    def RefillDeck(self):
        self.cards.append(self.staple)
        self.staple = []
        self.Shuffle()

    def Shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
        self.cards = []

    def as_string(self):
        results = self.name
        for card in self.cards:
            results = results, self.card[0].as_string()
        return results

    def draw_card(self, deck):
        self.cards.append(deck.draw_card())

new_game = CardDeck()
p1 = Player("Thomas", 1)
p2 = Player("Max", 2)
p3 = Player("Franz", 3)


my_cards = new_game.cards
for card in my_cards:
    print(card.as_string())


print('Draw card: ' + new_game.draw_card().as_string() + '  Abhebestapel: ' +
      str(len(new_game.cards)), 'Ablagestapel: ' + str(len(new_game.staple)))
print('Draw card: ' + new_game.draw_card().as_string() + '  Abhebestapel: ' +
      str(len(new_game.cards)), 'Ablagestapel: ' + str(len(new_game.staple)))
print('Draw card: ' + new_game.draw_card().as_string() + '  Abhebestapel: ' +
      str(len(new_game.cards)), 'Ablagestapel: ' + str(len(new_game.staple)))

new_game.RefillDeck()

print('Draw card: ' + new_game.draw_card().as_string() + '  Abhebestapel: ' +
      str(len(new_game.cards)), 'Ablagestapel: ' + str(len(new_game.staple)))


def deal_cards(deck, players):
    for i in range(7):
        for player in players:
            player.draw_card(deck)


deal_cards(new_game, [p1, p2, p3])

for card in p1.cards:
    print(p1.name + ': ' + card.as_string())
