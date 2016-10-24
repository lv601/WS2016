class Player:
    #Attributes: name ip-address cards other_player next_player
    def __init__(self, player, ip, cards, next_user, other_user):
        self.name=name
        self.ip=ip
        self.cards=cards  #cards in the hand
        self.next_user=next_user
        self.other_user=other_user

    def call_attribute_messages(self, ip, cards):
        #talk with server, messages required
        pass

    def ask_name(self, player):
        #unique name
        player=input("Please enter your user name: ")
        #vergleiche mit datenbank/liste/session
        return player

if __name__=="__main__":
    print(__file__)