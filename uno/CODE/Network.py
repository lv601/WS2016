import selectors
import socket
import pickle

class Network:
    def __init__(self, port, remote_port, ip_address=None, remote_ip_address=None):
        """
        Create a listener and a receiver socket pair
        :param port: locale instance port
        :param remote_port: remote instance port
        :param ip_address: locale ip address
        :param remote_ip_address: remote ip address
        """
        self.port = port
        self.remote_port = remote_port
        self.selectors = selectors.DefaultSelector()
        self.connected_clients = set()

        if remote_ip_address:
            self.remote_ip = remote_ip_address
        else:
            self.remote_ip = self.get_ip_address()

        if ip_address:
            self.ip = ip_address
        else:
            self.ip = self.get_ip_address()


    @staticmethod  # similar to staticmethod(get_ip_address)
    def get_ip_address():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Try to connect to googles DNS server
            sock.connect(("8.8.8.8", 80))
            # return network ip address
            return sock.getsockname()[0]

    def send_message(self, addr, message, buffer_size=4096):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("send_message:", addr, self.remote_port)
            s.connect((addr, self.remote_port))
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
        print("{} - Listen on port {}: ".format(self.ip, self.port))
        sock.bind((self.ip, self.port))
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