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
from PyQt5.QtWidgets import QApplication

from Message import Message
from Network import Network
from gui import ZUNO

__version__ = "v0.1"

DEBUG = False

def server(args):
    """
    Run app as deamon process
    :param args:
    :return:
    """
    print("Start ZUNO game as server on port {}".format(args.server_port))

    WAIT_FOR_PLAYER = True
    player_list = {}

    n = Network(args.server_port)

    def callback(conn, data):
        nonlocal WAIT_FOR_PLAYER

        # Unpickle data
        msg = pickle.loads(data)

        if DEBUG:
            print(msg)

        # Registry players
        if msg.type == "REGISTER":
            if WAIT_FOR_PLAYER:
                player_list[msg.sender[0]] = msg.sender[1:]
                print("Login player {}:{}:{}".format(*msg.sender))

                respond = Message("REGISTER", args.players - len(player_list), [msg.sender[0], n.ip, n.port], "Server", player_list)
                for nick in player_list:
                    print(nick)
                    if len(player_list) >= args.players:
                        WAIT_FOR_PLAYER = False
                        respond.msg = "FINISHED"

                    n.send_message(*player_list[nick], pickle.dumps(respond))
        elif msg.type == "UNREGISTER":
            print(msg)
            del player_list[msg.sender[0]]

            msg.data = player_list
            for nick in player_list:
                n.send_message(*player_list[nick], pickle.dumps(msg))
        elif msg.type == "CHAT":

            if msg.recipient == "all":
                for nick in player_list:
                    # Do not send back message to sender
                    if nick == msg.sender[0]:
                        continue
                    n.send_message(*player_list[nick], pickle.dumps(msg))
            else:
                n.send_message(*player_list[msg.recipient], pickle.dumps(msg))



        # If no client is connected stop server
        if player_list is None:
           n.stop_listen_socket()

        conn.close()
        n.selectors.unregister(conn)

    # Create and start server listening socket
    n.create_listen_socket(callback)
    n.run_listen_socket()


def client(args):
    """
    Run as client
    :param args:
    :return:
    """
    # Create socket instance
    n = Network(args.client_port)
    args.client_ip = n.ip

    def callback(conn, response, comm):
        msg = pickle.loads(response)
        comm.signal.emit(msg)
        conn.close()
        n.selectors.unregister(conn)

    n.create_listen_socket(callback)

    # Create GUI
    app = QApplication([args])
    gui = ZUNO(app, n, args)

    # Start Gui main loop
    return gui.run()


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
        parser_server.add_argument('-p', '--server-port', type=int, default=6010, help="Set remote server port. Default: 6010")
        parser_server.add_argument('-i', '--server-ip', type=str, default=None, help="Remote Server IP-address. Default: Host IP-address")
        parser_server.add_argument('-c', '--players', type=int, default=2, help="Number of players to wait. Default: 2")
        parser_server.set_defaults(func=server)

        parser_client = subparsers.add_parser('client', help='Start ZUNO game client')
        parser_client.add_argument('-p', '--client-port', type=int, default=6010, help="Set client port. Default: 6000")
        parser_client.add_argument('-i', '--server-ip', type=str, default=None, help="Remote Server IP-address. Default: Host IP-address")
        parser_client.add_argument('-r', '--server-port', type=int, default=6010, help="Set remote server port. Default: 6010")
        parser_client.add_argument('nickname', type=str, help="Player nickname. Must be unique in game")
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
