# Echo client program
import socket
import pickle

class foo:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "Foo: X = {0.X} Y = {0.Y}".format(self)

    def __bytes__(self):
        # Seralize object to bytes string
        return pickle.dumps(self)


if __name__ == "__main__":
    # Create data instance
    my_data = foo(10,14)
    print(my_data)

    HOST = 'localhost'    # The remote host
    PORT = 1235              # The same port as used by the server

    # Create client socket (IP4 TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # Send data to server
        s.sendall(bytes(my_data))  # bytes call __bytes__() Methode which pickles the object to bytes string
        # Wait for data from the server and close socket
        data = s.recv(1024)
        # Unpickle data back to foo instance
        print('Received', pickle.loads(data))
