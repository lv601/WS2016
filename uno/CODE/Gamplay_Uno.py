# to handle gameplay of card playing games

from random import randint
import Gameplay, Card_Deck, Card_Deck_Uno, Player, Rules_Uno

class Gameplay_Uno(Gameplay):
    def __init__(self):
        self.rules = Rules_Uno.rules()
        self.card_deck = Card_Deck_Uno.create_deck()
        self.rules = Rules_Uno()

    def draw_cards(self, available_card, number, draw_cards=[]):
        while number_to_draw <= number
        number_to_draw += 1
        random_number = randint(min(index(available_card)), max(index(available_card)))
        draw_cards = available_card[random_number].append
        available_card[random_number].pop

        return draw_cards

    def get_firtst_card(self,available_card):
        return  Gameplay_Uno.draw_cards(available_card, 1)


    def Number_of_cards(self, num_of_cards=[]):
        for Player.other_player:
            num_of_cards.append(Player.cards)



if __name__ == "__main__":
    gameplay()