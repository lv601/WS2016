import message

class Output:
    def __init__(self, message):
        self.message = message

    # shortcut für self.message.print
    def print(self, *args):
        self.message.print(*args)

    #########################################################

    #gibt "spieler sagt kommentar" aus
    def print_custom_text(self, player, text):
        self.print(str(player), "sagt:", text);

    # gibt Spielerzahl, Spielernamen und Anzahl der Startkarten aus
    def print_start_game(self, players, number_of_cards):
        self.print("Das Spiel beginnt mit", len(players), "Teilnehmern.")
        self.print("Jeder Spieler spielt mit", number_of_cards, "Startkarten.")
        for player in players:
            self.print(str(player), "nimmt am Spiel teil")

    # gibt Karten werden gemischt aus
    def print_shuffle_cards(self):
        self.print("Die Karten werden gemischt...")

    #gibt Spieler Name + zieht N Karten aus
    def print_draw_cards(self, number_of_cards, player=None):
        if (player == None):
            self.print("Du ziehst", number_of_cards, "Karten")
        else:
            self.print(str(player), "zieht", number_of_cards, "Karten")

    # gibt Spieler Name + Kartenhand aus (falls player = None wird kein name ausgegegben)
    def print_player_cards(self, cards, player=None):
        if (player == None):
            self.print("Deine Karten sind:")
        else:
            self.print(str(player), "hat folgende Karten:")
        for card in cards:
            self.print(str(card))

    # gibt aktuell liegende Karte aus
    def print_current_card(self, card):
        self.print("Es liegt:",str(card))

    # gibt aus welcher Spieler an der Reihe ist
    def print_turn(self, player=None):
        if (player == None):
            self.print("**** DU bist am Zug! ****")
        else:
            self.print(str(player), "ist am Zug")

    # fordert den Spieler auf eine Karte zu spielen
    def print_select_card_to_play_or_draw(self):
        self.print("Spiele eine Karte aus oder ziehe eine Karte")

    # diese Karte kann nicht gespielt werden
    def print_selected_card_not_allowed(self):
        self.print("Diese Karte kann nicht gespielt werden!")

    # gibt Spieler + gespielte Karte aus (card = None, passt)
    def print_plays_card(self, player, card=None):
        if (card == None):
            self.print(str(player), "passt.")
        else:
            self.print(str(player), "spielt folgende Karte: ", str(card))

    # gibt "UNO" Meldung aus (falls der Spieler die vorletzte Karte legt und dies bekannt gibt)
    def print_uno(self, player):
        self.print(str(player), "schreit: UNO")

    #gibt betroffene Spielernamen + challenge aus (falls gegen eine +4 Karte Einspruch erhoben wird)
    def print_challenge(self, active_player, challenging_player):
        self.print(str(challenging_player), "fordert", str(active_player), "seine Karten zu zeigen")

    #fragt welche Farbe gewählt werden soll
    def print_choose_color(self):
        self.print("Wähle eine Farbe:")

    #gibt die gewählte Farbe aus
    def print_chosen_color(self, player, color):
        self.print(str(player), "wählt die Farbe:", str(color))

    #gibt den verlierer der challange aus
    def print_challenge_result(self, player=None):
        if (player == None):
            self.print("Du verlierst die Herausforderung. Strafe folgt!")
        else:
            self.print(str(player), "verliert die Herausforderung und wird bestraft!")

    def print_current_card_number(self, cards, player=None):
        if (player == None):
            self.print("Du hast", len(cards),"Karten auf der Hand")
        else:
            self.print(str(player), "hat", len(cards), "Karten auf der Hand")

    # gibt "erwischt" aus falls der Spieler "Uno" vergessen hat
    def print_uno_tilt(self, player=None):
        if (player == None):
            self.print("Du wurdest erwischt! Strafe folgt!")
        else:
            self.print(str(player), "wurde erwischt und wird bestraft!")

    # gibt Rundenende und Rundensieger aus (letzte Karte abgelegt)
    def print_end_of_round(self, player=None):
        self.print("Die Runde ist zu Ende!")
        if (player == None):
            self.print("DU bist Rundensieger")
        else:
            self.print(str(player), "ist Rundensieger")

    # gibt Spielende und Spielsieger aus (Punkte erreicht)
    def print_end_of_game(self, player=None):
        self.print("Das Spiel ist zu Ende!")
        if (player == None):
            self.print("DU HAST GEWONNEN")
        else:
            self.print(str(player), "hat gewonnen")

    # gibt aktuellen Punktestand pro Spieler aus
    def print_scores(self, scores):
        self.print("Aktueller Punktestand")
        for player, score in scores:
            self.print(str(player), "hat:", str(score), "Punkte")



if __name__ == "__main__":
    #---------------------------------------
    #define some dummy class implementations
    class Player:
        def __init__(self):
            self.name = "TestSpieler(in)"
        def __repr__(self):
            return "Player";
        def __str__(self):
            return self.name

    class Card:
        def __init__(self):
            self.color = "Rot"
            self.symbol = "+2"
            self.action = ""
        def __repr__(self):
            return "Card";
        def __str__(self):
            return self.color+" "+self.symbol

    class Cards:
        def __init__(self):
            self.cards = [Card(), Card(), Card()]
        def __repr__(self):
            return "Cards";
        def __iter__(self):
            for card in self.cards:
                yield card
        def __len__(self):
            return len(self.cards)

    #---------------------------------------
    #test functions
    out = Output( message.Message_Chat() )
    out.print_custom_text( Player(), "hallo ihr da!")
    out.print_start_game( [Player(),Player()] , 5)
    out.print_shuffle_cards()
    out.print_draw_cards(5, Player())
    out.print_draw_cards(5)
    out.print_player_cards(Cards(), Player())
    out.print_player_cards(Cards())
    out.print_current_card(Card())
    out.print_turn()
    out.print_turn(Player())
    out.print_select_card_to_play_or_draw()
    out.print_selected_card_not_allowed()
    out.print_plays_card(Player())
    out.print_plays_card(Player(), Card())

    out.print_uno(Player())
    out.print_challenge(Player(), Player())
    out.print_current_card_number(Cards())
    out.print_current_card_number(Cards(), Player())
    out.print_choose_color()
    out.print_chosen_color(Player(), "green")
    out.print_challenge_result(Player())
    out.print_challenge_result()
    out.print_uno_tilt(Player())
    out.print_uno_tilt()


    out.print_end_of_round(Player())
    out.print_end_of_round()
    scores = {(Player(), 100), (Player(), 200)}
    out.print_scores(scores)
    out.print_end_of_game(Player())
    out.print_end_of_game()
