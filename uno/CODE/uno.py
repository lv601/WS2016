#! /usr/bin/env python3
# encoding: utf-8
"""
ZUNO - Server
Playing Uno or other card games over the network

@authors:   Alexander Bindeus, Bianca Allegra Buchner, Julie Krainer, Anna Majewski, Clemens Spielvogel, Shelley Mangan,
            Alexander Tolios, Claudia Juno, Michael Lehrach, Thomas Schwarz, Jose Basilio, Frank Ruge, Alma Beganovic,
            Anna Tomaselli, Tamas Gutsohnn, Eva Niessner, Stefan Rieger, Martin Gollobich, Norbert Auer

@license:    GPL 3.0

@contact:    norbert.auer@boku.ac.at
"""

import sys
import pickle
from argparse import ArgumentParser
from Network import Network
from threading import Thread
import time

__version__ = "v0.1"

DEBUG = False

class Output:
    def update(self, msg):
        print("I'm an instance of class Output:", msg)

class Message:
    def __init__(self, type, msg, sender, recipient="all", data=None):
        self.type = type
        self.msg = msg
        self.data = data
        self.sender = sender
        self.recipient = recipient

def server(args):
    """
    Run app as deamon process
    :param args:
    :return:
    """
    print("Start ZUNO game as server on port {}".format(args.server_port))

    WAIT_FOR_PLAYER = True
    player_list = {}

    n = Network(args.client_port, args.server_port)

    def callback(conn, data):
        nonlocal WAIT_FOR_PLAYER

        # Unpickle data
        msg = pickle.loads(data)

        if WAIT_FOR_PLAYER:
            # Registry players
            if msg.type == "WAIT_FOR_PLAYER":
                player_list[msg.msg] = msg.sender
                print("Login player {}:{}".format(msg.msg, msg.sender))
                if len(player_list) >= 2:
                    WAIT_FOR_PLAYER = False
        else:
            if msg.type == "CHAT":
                if msg.recipient == "all":
                    for addr in n.connected_clients:
                        print("Send message '{}' to: {}".format(msg.msg, addr))
                        n.send_message(addr, msg.msg.encode())
                else:
                    print("Send message '{}' to: {}:{}".format(msg.msg, msg.recipient, player_list[msg.recipient]))
                    n.send_message(player_list[msg.recipient], msg.msg.encode())

        conn.close()
        n.selectors.unregister(conn)

    n.create_listen_socket(callback)

    n.run_listen_socket()


def client(args):
    """
    Run as client
    :param args:
    :return:
    """
    print("Player {} start ZUNO game as client on port {}".format(args.nickname, args.client_port))

    n = Network(args.client_port, args.server_port, remote_ip_address=args.server_ip)
    ref = Output()

    def callback(conn, msg):
        ref.update(msg)

        conn.close()
        n.selectors.unregister(conn)

    n.create_listen_socket(callback)

    # Start client listening server
    t1 = Thread(target=n.run_listen_socket)
    t1.start()

    # Login
    msg = Message("WAIT_FOR_PLAYER", args.nickname, n.ip, "")
    n.send_message(n.remote_ip, pickle.dumps(msg))

    # Start main loop
    while True:
        inp = input("Eingabe: ")
        inp2 = input("Senden an: ")

        msg = Message("CHAT", inp, {args.nickname:n.ip}, inp2)

        n.send_message(n.remote_ip, pickle.dumps(msg))

        time.sleep(1)

def main(argv=None):
    """ Command line options """

    # Debug parameter
    if DEBUG:
        # Server
        sys.argv.append("server")
        sys.argv.append("-p")
        sys.argv.append("6010")

        sys.argv.append("client")
        sys.argv.append("--server-ip")
        sys.argv.append("141.244.113.120")

        # Client
        # sys.argv.append("-r")
        # sys.argv.append("7012")
        # sys.argv.append("-p")
        # sys.argv.append("7002")
        # sys.argv.append("nauer")
        pass

    if argv:
        sys.argv.extend(argv)

    if len(sys.argv) == 1:
        sys.argv.append("--help")

    try:
        # Setup argument parser
        parser = ArgumentParser()
        parser.add_argument('-V', '--version', action='version', version=__version__)
        subparsers = parser.add_subparsers(help='sub-command help')

        parser_server = subparsers.add_parser('server', help='Start ZUNO game server')
        parser_server.add_argument('-p', '--server-port', type=int, default=6010, help="Set remote server port. Default = 6010")
        parser_server.add_argument('-i', '--server-ip', type=str, default=None, help="Remote Server IP-address. Default = Host IP-address")
        parser_server.set_defaults(func=server)

        parser_client = subparsers.add_parser('client', help='Start ZUNO game client')
        parser_client.add_argument('-p', '--client-port', type=int, default=6010, help="Set client port. Default = 6000")
        parser_client.add_argument('-i', '--server-ip', type=str, default=None, help="Remote Server IP-address. Default = Host IP-address")
        parser_client.add_argument('-r', '--server-port', type=int, default=6010, help="Set remote server port. Default = 6010")
        parser_client.add_argument('nickname', type=str, help="Player nickname. Must be unique")
        parser_client.set_defaults(func=client)

        # Process arguments
        args = parser.parse_args()

        return args.func(args)

    except KeyboardInterrupt:
        ### Handle keyboard interrupt ###
        return 0
    except Exception as e:
        sys.stderr.write("ZUNO - Server: " + repr(e) + "\n")
        sys.stderr.write("  for help use --help")
        raise e

if __name__ == "__main__":
    sys.exit(main())
