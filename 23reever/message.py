class Message:
    def __init__(self, type):
        self.type = type
    def __repr__(self):
        return self.type
    def print(self):
        pass

class Message_Chat(Message):
    def __init__(self):
        super(Message_Chat,self).__init__("Message_Chat")
    def print(self, *args):
        print(*args)

class Message_App(Message):
    def __init__(self):
        super(Message_Chat, self).__init__("Message_App")
    def print(self, *args):
        #do something fancy
        pass


if __name__ == "__main__":
    test = Message_Chat()
    test.print("Hallo")
