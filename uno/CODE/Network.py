import selectors
import socket
import pickle

class Network:
    def __init__(self, client_port, server_port, client_ip_address=None, server_ip_address=None):
        self.c_port = client_port
        self.s_port = server_port
        self.selectors = selectors.DefaultSelector()
        self.connected_clients = set()

        if server_ip_address:
            self.s_host = server_ip_address
        else:
            self.s_host = self.get_ip_address()

        if client_ip_address:
            self.c_host = client_ip_address
        else:
            self.c_host = self.get_ip_address()


    @staticmethod  # similar to staticmethod(get_ip_address)
    def get_ip_address():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Try to connect to googles DNS server
            sock.connect(("8.8.8.8", 80))
            # return network ip address
            return sock.getsockname()[0]

    def send_message(self, addr, message, buffer_size=4096):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((addr, self.c_port))
            # Send data to server
            s.sendall(message)
            s.close()

    def create_listen_socket(self, callback, buffer_size=4096):
        # Accept connection to socket sock
        def accept(sock, mask):
            conn, addr = sock.accept()  # Should be ready

            # Add client-adress to client list
            # Remove clients only when the socket can not connect
            self.connected_clients.add(conn.getpeername()[0])
            conn.setblocking(False)
            # Register callback function read for conn
            self.selectors.register(conn, selectors.EVENT_READ, read)

            # Data is send to socket sock

        def read(conn, mask):
            data = conn.recv(buffer_size)  # Should be ready)
            callback(conn, data)

        sock = socket.socket()
        print("Listen on port {}: ".format(self.s_port))
        sock.bind((self.s_host, self.s_port))
        sock.listen(100)
        # Allows muliple connections at the same time
        sock.setblocking(False)

        # Register callback function accept() for sock
        self.selectors.register(sock, selectors.EVENT_READ, accept)

    def run_listen_socket(self):
        while True:
            events = self.selectors.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)


if __name__ == "__main__":
    n = Network(6010, 6000)

    def callback(conn, data):
        for addr in n.connected_clients:
            n.send_message(addr, data)

        conn.close()
        n.selectors.unregister(conn)

    n.create_listen_socket(callback)

    n.run_listen_socket()