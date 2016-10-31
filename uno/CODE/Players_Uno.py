## Date: 20.10.2016 -
## Authors: Alma Beganovic, Claudia Juno, Anna Majewski, Shelley Mangan
## Description: Player Module for UNO game project

user_list = []  #in case of deleting list upon add_new_player
class Player:
    #Attributes: name ip-address cards other_player next_player
    def __init__(self, player, ip, cards, next_user, other_user):
        self.name = name
        self.ip = ip
        self.cards = cards  #cards in the hand
        self.next_user = next_user
        self.other_user = other_user

    def call_attr_msg(self, ip, cards):
        #talk with server, messages required
        pass

    def ask_name(self, player):
        #unique name!
        player = input("Please enter your user name: ")
        while player in user_list:
           print("This name has been taken.")
           self.ask_name
        else:
            return player
        

    def add_user(self, player):
        if player in user_list:
            pass
        else:
            user_list.append

if __name__ == "__main__":
    print(__file__)
