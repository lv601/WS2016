#from UNO_Players import Player as player
#Player müssen importiert werden

players = [{"name":"test1", "ip":123}, {"name": "juulie", "ip": 345}, {"name": "testest", "ip": 666}]

class GamePlay:
    def __init__(self, player):
        self.player = player
        self.queue = []
        self.queue = self.add_to_queue()
        self.clock_wise = True
        print(self.queue)
    def add_to_queue(self):
        for i in range(len(self.player)):
            self.queue.append(self.player[i]["ip"])
        return self.queue
    def change_dir(self):
        self.clock_wise = [not self.clock_wise]
        self.queue = list(reversed(self.queue))
        if self.clock_wise == True:
            print("Die Reihenfolge hat sich geändert! Es wird im Uhrzeigersinn gespielt")
        else:
            print("Die Reihenfolge hat sich geändert! Es wird gegen den Uhrzeigersinn gespielt")
        return self.clock_wise, self.queue
    def next_player(self):
        curr_player = self.queue.pop()
        self.queue.append(curr_player)
        return self.queue

bla = GamePlay(players)
print(bla.add_to_queue())
print(bla.change_dir())
print(bla.next_player())


#    def __init__(self):
#        self.queue = []
#        self.clock_wise = True; #Auf True, außer wenn die Spezial Karte ausgespielt wird
#    player_queue = [p1, .. , p10] #Die Reihenfolge der SpielerInnen
#    card_deck = Card_Deck # Ein neues Kartendeck wird initiiert
#    rules = Rules() # Die Spielregeln werden initiiert
#    current_card = Card() #welche Karte ist gerade die oberste auf dem Stapel?#

    #def shuffle_cards(): #Die Karten sollen gemischt werden
    #def deal_cards(number_cards):

    #def player_queue():



#shuffle_cards()
#draw_cards(number_cards=1)
#play_card(number_cards=1)
#deal_cards(number_cards)
#wait_for_player()
#start_game()

#class GamePlay_Uno(GamePlay):
#    def __init__(self):
#        card_deck = card_deck_Uno
#        number_of_cards
#        rules = Rules_Uno()
#    def get_first_card(self):

#    def draw_cards(self):

