import selectors
import select
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



sel = selectors.DefaultSelector()

# Accept connection to socket sock
def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    # Register callback function read for conn
    sel.register(conn, selectors.EVENT_READ, read)


# Data is send to socket sock
def read(conn, mask):
    # Read max.1024 bytes
    data = conn.recv(1024)  # Should be ready
    if data:
        # Unpickle data to foo instance
        my_foo = pickle.loads(data)
        print('echoing {} to {}'.format(my_foo, conn))
        my_foo.Y = 100
        # Send data back
        conn.send(bytes(my_foo))  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('141.244.83.209', 1235))
sock.listen(100)
# Allows muliple connections at the same time
sock.setblocking(False)

# Register callback function accept() for sock
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)