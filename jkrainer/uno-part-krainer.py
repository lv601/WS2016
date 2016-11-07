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
