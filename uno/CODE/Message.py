class Message:
    def __init__(self, type, msg, sender, recipient="all", data=None):
        self.type = type
        self.msg = msg
        self.data = data
        # Sender is defined as [nickname, ip-address, listening port]
        self.sender = sender
        self.recipient = recipient

    def __str__(self):
        return "\nMESSAGE\nType: {0.type}\nMessage: {0.msg}\nData: {0.data}\nFrom: {0.sender}\nTo: {0.recipient}".format(self)