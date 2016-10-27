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
DEBUG = True

class Output:
    def update(self, msg):
        print("I'm an instance of class Output:", msg)

class Message:
    def __init__(self, type, msg, sender, recipient="all"):
        self.type = type
        self.msg = msg
        self.sender = sender
        self.recipient = recipient

def start(args):
    if DEBUG:
        print(args)

    # Run as game server or client
    if args.daemon:
        server(args)
    else:
        client(args)

def server(args):
    """
    Run app as deamon process
    :param args:
    :return:
    """
    print("Start ZUNO game as server on port {}".format(args.server_port))

    n = Network(args.client_port, args.server_port)

    def callback(conn, data):
        # Unpickle data
        msg = pickle.loads(data)

        if msg.recipient == "all":
            for addr in n.connected_clients:
                print("Send message '{}' to: {}".format(msg.msg, addr))
                n.send_message(addr, msg.msg.encode())

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
    print("Start ZUNO game as client on port {}".format(args.client_port))

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

    # Start main loop
    while True:
        inp = input("Eingabe: ")

        msg = Message("chat", inp, n.port)

        n.send_message(n.remote_ip, pickle.dumps(msg))

        time.sleep(1)

def main(argv=None):
    """ Command line options """

    # Debug parameter
    if DEBUG:
        sys.argv.append("--server-ip")
        sys.argv.append("141.244.113.120")

        # sys.argv.append("-d")
        # sys.argv.append("-r")
        # sys.argv.append("7001")
        # sys.argv.append("-p")
        # sys.argv.append("7011")

        sys.argv.append("-r")
        sys.argv.append("7001")
        sys.argv.append("-p")
        sys.argv.append("7011")
        pass

    if argv:
        sys.argv.extend(argv)

    if len(sys.argv) == 1:
        sys.argv.append("--help")

    try:
        # Setup argument parser
        parser = ArgumentParser()
        parser.add_argument('-V', '--version', action='version', version=__version__)
        parser.add_argument('-p', '--client-port', type=int, default=6000, help="Set local server port. Default = 6000")
        parser.add_argument('-r', '--server-port', type=int, default=6010, help="Set remote server port. Default = 6010")
        parser.add_argument('-i', '--server-ip', type=str, default=None, help="Remote Server IP-address. Default = Host IP-address")
        parser.add_argument('-d', '--daemon', action="store_true", help="Run as game server")

        # Process arguments
        args = parser.parse_args()

        return start(args)

    except KeyboardInterrupt:
        ### Handle keyboard interrupt ###
        return 0
    except Exception as e:
        sys.stderr.write("ZUNO - Server: " + repr(e) + "\n")
        sys.stderr.write("  for help use --help")
        raise e

if __name__ == "__main__":
    sys.exit(main())