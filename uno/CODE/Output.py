# Included classes: Output
from Gameplay import current_card, player_cards
import Card_deck

class Output:
    def print_current_card(self):
        return Gameplay.current_card

    def print_player_cards(self):
        for card in player_cards:
            return card


# myDeck = Card_deck.Deck_Uno()
# myDeck.create_deck()
#
# player_cards = []
# player_cards.append(myDeck.deck[0:4])
#
# output = Output()
# for card in output.print_player_cards():
#     print(card.color, card.symbol, card.action)
