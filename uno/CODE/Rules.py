# Included classes: Rules_Uno
# Weiterreichen der zusaetzlich gezogenen Karten
import Player

class Rules_Uno:
    def draw2(self):
        draw_cards(number_cards=2) # Set current Player

    def reverse(self):
        if GamePlay.clock_wise == True:
            GamePlay.clock_wise = False
        else:
            GamePlay.clock_wise = True

    def skip(self):
        Player.current_player += 1 # Cave, current_player variable, Player Instanz Name

    def wildcard(self):
        valid = False
        while valid = False
            self.new_color = input("What color would you like to set?\nr...red\ny...yellow\ng...green\nb...blue\n")
            valid = True
            if self.new_color == 'r':
                self.color = 'red'
            elif self.new_color == 'y:
                self.color = 'yellow'
            elif self.new_color == 'g':
                self.color = 'green'
            elif self.new_color == 'b':
                self.color = 'blue'
            else:
                valid = False

        return self.color

    def wildcard4(self):
        draw_cards(number_cards=4) # Set current Player
        valid = False
        while valid = False
            self.new_color = input("What color would you like to set?\nr...red\ny...yellow\ng...green\nb...blue\n")
            valid = True
            if self.new_color == 'r':
                self.color = 'red'  # edit color var
            elif self.new_color == 'y:
                self.color = 'yellow'
            elif self.new_color == 'g':
                self.color = 'green'
            elif self.new_color == 'b':
                self.color = 'blue'
            else:
                valid = False
