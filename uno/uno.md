# UNO

## Klassen
# Juno, Majewski, Mangan, Beganovic
class Player:
  name
  ip-address
  cards
  other_player
  next_player

# Ruge, Lehrach, Krainer
class GamePlay:
  player_queue = [p1, .. , p10]
  clock_wise = True
  card_deck = Card_Deck
  rules = Rules()
  current_card = Card()
  
  shuffle_cards()
  draw_cards(number_cards=1)
  play_card(number_cards=1)
  deal_cards(number_cards)
  wait_for_player()
  start_game()
  
 
class GamePlay_Uno(GamePlay):
  number_of_cards
  get_first_card()
  draw_cards()
  card_deck = Card_Deck_Uno
  rules = Rules_Uno()

# Spielvogel, Basilio, gollobich, Rieger, Tolios
class Card:
color=
symbol
action

class Card_Uno(Card):



class Card_Deck:
  cards = [Card_Uno, ...]
  create_deck()

class Card_Deck_Uno:
  create_deck()


class Rules:


class Rules_Uno(Rules):

Card1 = Card("")

class Output:
  print_player_cards()
  print_current_card()

# Buchner
class Message:
  type
  

class Message_Chat(Message):


class Message_App(Message):

# Schwarz, Gutsohn
class Network:
  
