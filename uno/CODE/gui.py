#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QComboBox)
from PyQt5.QtGui import (QColor, QTextCharFormat)
from PyQt5.QtCore import (pyqtSignal, QObject)
from threading import Thread
from Message import Message
import socket
import pickle

class Communicate(QObject):
    signal = pyqtSignal(Message)

class ZUNO(QWidget):
    def __init__(self, app, network, args):
        super().__init__()

        self.comm = Communicate()
        self.comm.signal.connect(self.process_message)
        self.app = app
        self.n = network
        self.args = args
        self.player = {args.nickname:[args.client_port, args.client_ip]}
        self.initUI()

    def initUI(self):
        lbl = QLabel("Send message to:")
        lbl2 = QLabel("Chat Log:")
        self.textbox = QLineEdit()

        self.button = QPushButton()
        self.button.setText("Send")
        self.button.clicked.connect(self.send)

        self.combo = QComboBox()
        self.combo.addItem("all")
        self.combo.addItems(self.player)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        # self.log.setLineWrapMode(QTextEdit.NoWrap)
        self.log_cursor = self.log.textCursor() #QTextCursor(self.log.document())
        self.format = QTextCharFormat()
        self.format.setForeground(QColor('black'))

        layoutV = QVBoxLayout(self)
        layoutH = QHBoxLayout()

        layoutH.addWidget(self.textbox)
        layoutH.addWidget(self.combo)
        layoutH.addWidget(self.button)

        layoutV.addWidget(lbl)
        layoutV.addLayout(layoutH)
        layoutV.addWidget(lbl2)
        layoutV.addWidget(self.log)
        layoutV.addStretch()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('ZUNO')

    # If window is destroyed
    def closeEvent(self, event):
        self.n.stop_listen_socket()
        msg = Message("UNREGISTER", "", [self.args.nickname, self.n.ip, self.n.port], "")
        self.n.send_message(self.args.server_ip, self.args.server_port, pickle.dumps(msg))



    # Run Gui
    def run(self):
        self.show()

        # Start client listening server
        t1 = Thread(target=self.n.run_listen_socket, args=[self.comm])
        t1.start()

        # Register player at server
        msg = Message("REGISTER", "", [self.args.nickname, self.n.ip, self.n.port], "")

        try:
            print("Send message to {0.server_ip}:{0.server_port}".format(self.args))
            self.n.send_message(self.args.server_ip, self.args.server_port, pickle.dumps(msg))
        except socket.timeout:
            print("Can not connect to server {0.server_ip}:{0.server_port}. Connection timeout!".format(self.args),
                  file=sys.stderr)
            self.n.stop_listen_socket()

        return(self.app.exec_())

    def process_message(self, msg):
        if msg.type == "REGISTER":
            self._update_combobox(msg.data)

            # Send message to log box
            self.log.setTextColor(QColor("red"))
            self.log.append("Player {} has logged in! {} players missing.".format(msg.sender[0], msg.msg))

            if msg.msg == "FINISHED":
                self.log.append("Enough player are connected. Start the game")

        if msg.type == "CHAT":
            self.log.setTextColor(QColor("green"))
            self.log.append("{}".format(msg.sender[0]))
            self.log_cursor.insertText(": {} [{}]".format(msg.msg, msg.recipient), self.format)
        elif msg.type == "UNREGISTER":
            self._update_combobox(msg.data)

            # Send message to log box
            self.log.setTextColor(QColor("red"))
            self.log.append("Player {} has quit the game. Shame on him...".format(msg.sender[0]))




    def send(self, event):
        msg = Message("CHAT", self.textbox.text(), [self.args.nickname, self.n.ip, self.n.port], self.combo.currentText())

        try:
            self.n.send_message(self.args.server_ip, self.args.server_port, pickle.dumps(msg))
            self.log.setTextColor(QColor("orange"))
            self.log.append("{}".format(msg.sender[0]))
            self.log_cursor.insertText(": {} [{}]".format(msg.msg, self.combo.currentText()), self.format)
        except socket.timeout:
            print("Can not connect to server {0.server_ip}:{0.server_port}. Connection timeout!".format(self.args),
                  file=sys.stderr)
            self.n.stop_listen_socket()
            exit(-1)

    def _update_combobox(self, player):
        self.player = player

        # Update combobox
        self.combo.clear()
        self.combo.addItem("all")

        for player in self.player:
            self.combo.addItem(player)

if __name__ == '__main__':
    ex = ZUNO()

    ex.run((sys.argv))

