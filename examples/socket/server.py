import selectors
import socket
import pickle

from client import foo

HOST = '141.244.134.225'
PORT = 5002
PORT2= 5003

sel = selectors.DefaultSelector()

connected_clients = set()

def chat(stream, mask):
    print(stream.readline())


# Accept connection to socket sock
def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready

    # Add client-adress to client list
    # Remove clients only when the socket can not connect
    connected_clients.add(conn.getpeername()[0])
    conn.setblocking(False)
    # Register callback function read for conn
    sel.register(conn, selectors.EVENT_READ, read)


# Data is send to socket sock
def read(conn, mask):
    data = conn.recv(4096)  # Should be ready)

    for addr in connected_clients:
        # Create send sockets to all clients
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((addr, PORT2))
            print(data, addr)
            # Send data to server
            s.sendall(data)
            s.close()
    conn.close()
    sel.unregister(conn)


sock = socket.socket()
sock.bind((HOST, PORT))
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