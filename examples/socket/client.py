# Echo client program
import socket
import pickle
from threading import Thread
import selectors


HOST = '141.244.134.225' # The remote host
LOKAL_HOST = '141.244.134.225'

PORT = 5002              # (Sending) The same port as used by the server
PORT2= 5003              # (Receiving)


class foo:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "Foo: X = {0.X} Y = {0.Y}".format(self)

    def __bytes__(self):
        # Seralize object to bytes string
        return pickle.dumps(self)


class output:
    def update(self, msg):
        print("I'm an instance of class Output:", msg)


# Create listening server - runs in it own thread
def create_socket(ref):
    sel = selectors.DefaultSelector()

    # Accept connection to socket sock
    def accept(sock, mask):
        conn, addr = sock.accept()  # Should be ready
        # conn.setblocking(False)
        # Register callback function read for conn
        sel.register(conn, selectors.EVENT_READ, read)

    # Data is send to socket sock
    def read(conn, mask):
        # Read max.1024 bytes
        data = conn.recv(4096)  # Should be ready

        # Do something with the received data
        ref.update(data)

        sel.unregister(conn)
        conn.close()

    sock = socket.socket()
    sock.bind((LOKAL_HOST, PORT2))
    sock.listen(1)  # Only listen to server

    # Allows muliple connections at the same time
    # sock.setblocking(False)

    # Register callback function accept() for sock
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)


if __name__ == "__main__":
    # Create data instance
    my_data = foo(10,14)
    print(my_data)

    ref = output()  # Replace by output instance

    # Start client listening server
    t1 = Thread(target=create_socket, args=(ref,))
    t1.start()

    # Application main loop
    while True:
        msg = input("Eingabe: ")

        # Create client socket (IPv4 TCP socket) - Send message to server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # Send data to server
            s.sendall(msg.encode())  # bytes call __bytes__() Methode which pickles the object to bytes string
            s.close()


