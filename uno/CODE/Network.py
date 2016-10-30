import selectors
import socket
import sys

class Network:
    def __init__(self, port, ip_address=None):
        """
        Create a listener and a receiver socket pair
        :param port: listen port
        :param ip_address: locale ip address
        :param remote_ip_address: remote ip address
        """
        self.port = port
        self.selectors = selectors.DefaultSelector()

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
            s.connect((remote_ip, remote_port))
            # Send data to server
            s.sendall(message)

            s.close()

    def create_listen_socket(self, callback, buffer_size=4096):
        # Accept connection to socket sock
        def accept(sock, mask, comm=None):
            conn, addr = sock.accept()  # Should be ready

            #conn.setblocking(False)
            # Register callback function read for conn
            self.selectors.register(conn, selectors.EVENT_READ, read)
            # Data is send to socket sock

        def read(conn, mask, comm=None):
            msg = bytearray()

            data = None

            # Read as long data is sended
            while data != b"":
                try:
                    data = conn.recv(buffer_size)
                    msg += data
                except BlockingIOError:
                    print("Got BlockingIOError", file=sys.stderr)
                    time.sleep(1)
            if comm:
                callback(conn, msg, comm)
            else:
                callback(conn, msg)

        sock = socket.socket()
        sock.settimeout(3)
        print("{} - Listen on port {}: ".format(self.ip, self.port))
        sock.bind((self.ip, self.port))
        sock.listen(100)
        # Allows muliple connections at the same time
        sock.setblocking(False)

        # Register callback function accept() for sock
        self.selectors.register(sock, selectors.EVENT_READ, accept)

    def run_listen_socket(self, comm=None):
        print("Run_listen:", comm)
        while True:
            if self._stop:
                break
            events = self.selectors.select()
            for key, mask in events:
                callback = key.data
                if comm:
                    callback(key.fileobj, mask, comm)
                else:
                    callback(key.fileobj, mask)
        print("Close listening socket")

    def stop_listen_socket(self):
        self._stop = True
        self.send_message(self.ip, self.port, b"Close socket")


if __name__ == "__main__":
    from threading import Thread
    import time

    # Socket 1
    n1 = Network(5020)
    n1.remote_ip = n1.ip

    def callback1(conn, data):
        print("n1 receive:", data.decode(), conn)

        conn.close()
        n1.selectors.unregister(conn)

    n1.create_listen_socket(callback1)

    # Socket 2
    n2 = Network(5070)
    n2.remote_ip = n2.ip


    def callback2(conn, data):
        print("n2 receive:", data.decode(), conn)

        conn.close()
        n2.selectors.unregister(conn)


    n2.create_listen_socket(callback2)

    # Start client listening server
    t1 = Thread(target=n1.run_listen_socket)
    t2 = Thread(target=n2.run_listen_socket)

    t1.start()
    t2.start()
    print("Thread 1 tid:", t1.ident)
    print("Thread 2 tid:", t2.ident)

    # Send messages from socket 1 to socket 2 and vice versa
    n1.send_message(n2.ip, n2.port, b"Hello World")
    n2.send_message(n1.ip, n1.port, b"Goodbye World")

    # Send close signal to stop listening socket and thread t1
    time.sleep(1)  # Wait to receive all messages before closing the sockets
    n1.stop_listen_socket()
    n2.stop_listen_socket()