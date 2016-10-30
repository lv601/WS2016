import selectors
import socket

class Network:
    def __init__(self, port, ip_address=None, remote_ip_address=None):
        """
        Create a listener and a receiver socket pair
        :param port: listen port
        :param ip_address: locale ip address
        :param remote_ip_address: remote ip address
        """
        self.port = port
        self.selectors = selectors.DefaultSelector()
        #self.connected_clients = set()

        if remote_ip_address:
            self.remote_ip = remote_ip_address
        else:
            self.remote_ip = self.get_ip_address()

        if ip_address:
            self.ip = ip_address
        else:
            self.ip = self.get_ip_address()

        # Is set to true when stop_signal is sent
        self._stop = False


    @staticmethod  # similar to staticmethod(get_ip_address)
    def get_ip_address():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Try to connect to googles DNS server
            sock.connect(("8.8.8.8", 80))
            # return network ip address
            return sock.getsockname()[0]

    def send_message(self, remote_ip, remote_port, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("send_message:", remote_ip, remote_port, message.decode())
            s.connect((remote_ip, remote_port))
            # Send data to server
            s.sendall(message)
            s.close()

    def create_listen_socket(self, callback, buffer_size=4096):
        # Accept connection to socket sock
        def accept(sock, mask):
            conn, addr = sock.accept()  # Should be ready

            # Add client-adress to client list
            # Remove clients only when the socket can not connect
            conn.setblocking(False)
            # Register callback function read for conn
            self.selectors.register(conn, selectors.EVENT_READ, read)
            # Data is send to socket sock

        def read(conn, mask):
            msg = bytearray()

            data = None

            # Read as long data is sended
            while data != b"":
                data = conn.recv(buffer_size)
                msg += data

            callback(conn, msg)

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
            if self._stop:
                break
            events = self.selectors.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)
        print("Close listening socket")

    def stop_listen_socket(self):
        self._stop = True
        self.send_message(self.ip, self.port, b"Close socket")



if __name__ == "__main__":
    n = Network(5000)
    n.remote_ip = n.ip

    def callback(conn, data):
        print(data.decode())

        conn.close()
        n.selectors.unregister(conn)

    n.create_listen_socket(callback)

    from threading import Thread

    # Start client listening server
    t1 = Thread(target=n.run_listen_socket)
    t1.start()

    n.send_message(n.remote_ip, n.port, b"Hello World"*3)
    n.send_message(n.remote_ip, n.port, b"Goodbye World"*3)

    # Send close signal
    n.stop_listen_socket()