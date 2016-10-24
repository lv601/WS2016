import socket
import sys
import pickle

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = "141.244.83.209" #sys.argv[1]
server_address = (server_name, 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)


class cMessage():
    def __init__(self,id, message):
        self.id = id
        self.data = message

    def __str__(self):
        return str(self.id) + " " + str(self.data)


test = cMessage("Thomas", "halo test")
print(test)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(16)
            #print('received "%s"' % data)
            pickle.un
            if data:
                connection.sendall(b'back' + data)
            else:
                break
    finally:
        connection.close()