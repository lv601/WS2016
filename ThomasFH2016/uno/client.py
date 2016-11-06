import select, socket, sys
from utils import Room, Hall, Player
import utils
import game


READ_BUFFER = 4096
TEST_HOST = '141.244.85.187'


#if len(sys.argv) < 2:
#    print("Usage: Python3 client.py [hostname]", file = sys.stderr)
#    sys.exit(1)
#else:
server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_connection.connect((TEST_HOST, utils.PORT)) #sys.argv[1], utils.PORT))

def prompt():
    print('>', end=' ', flush = True)

print("Connected to server\n")
msg_prefix = ''

socket_list = [sys.stdin, server_connection]

player1 = game.player("Thomas")

while True:
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    for s in read_sockets:
        if s is server_connection: # incoming message
            msg = s.recv(READ_BUFFER)
            if not msg:
                print("Server down!")
                sys.exit(2)
            else:
                if msg == utils.QUIT_STRING.encode():
                    sys.stdout.write('Bye\n')
                    sys.exit(2)
                elif b"<card>" in msg:
                    print("Got card:", msg[6:])
                elif msg == b"RETURNVALUE":
                    print("RECEIVED ANSWER FROM SERVER")
                else:
                    sys.stdout.write(msg.decode())
                    if 'Please tell us your name' in msg.decode():
                        msg_prefix = 'name: ' # identifier for name
                    else:
                        msg_prefix = ''
                    prompt()

        else:
            msg = msg_prefix + '(' + player1.id + ')' + sys.stdin.readline()
            server_connection.sendall(msg.encode())
