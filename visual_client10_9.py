# coding:utf-8

import socket
import threading
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLineEdit,QTextEdit,QLabel,QPushButton,QFrame
from PyQt5 import QtCore,QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import*
from PyQt5.QtGui import QIcon

host = 'localhost'
port = 9999
username = '12Dong'

class Log(QFrame):
    def __init__(self,s):
        super().__init__()
        self.initUI()
        self.s=s

    def initUI(self):
        self.setObjectName('main')
        self.Str = QLabel("Welcome to my chat room.Please input your nickname")
        self.Nickname = QLabel('Nickname : ')
        self.text = QLineEdit()
        self.btnStart = QPushButton("Start!")
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.Str,2,2,2,5)
        grid.addWidget(self.Nickname,3,1,3,1)
        grid.addWidget(self.text,3,2,3,4)
        grid.addWidget(self.btnStart,3,6,3,6)
        self.setLayout(grid)

        self.creationAction()
        self.setWindowTitle('Title')
        self.setGeometry(500, 500, 500, 300)
        with open('logbg.qss', 'r') as p:
            self.setStyleSheet(p.read())
        self.show()

    def setNickname(self):
        name =  str(self.text.text())
        self.text.setText('')
        s.send(name.encode('utf-8'))
        c = Client(name)
        c.show()
        self.close()
    def creationAction(self):
        self.btnStart.clicked.connect(self.setNickname)

class Client(QFrame):
    def __init__(self, name):
        super().__init__()
        self.Nickname = name
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Client')
        self.setNameWidget = QWidget()#
        self.layout = QGridLayout(self)#
        self.setNameLayout = QGridLayout(self.setNameWidget)#
        self.btnSend = QPushButton('send')#
        self.input = QLineEdit()#
        self.chat = QTextEdit()#

        self.timer = QtCore.QTimer()
        self.messages = []

        self.build()
        self.createAction()
        self.setWindowIcon(QIcon("mylove.ico"))
        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        recvThread = threading.Thread(target=self.recvFromServer) #
        recvThread.start()#

        self.setGeometry(500,500,600,400)
        self.setWindowTitle('Communcation')
        with open('texteditbg.qss', 'r') as q:
            self.setStyleSheet(q.read())

    def sendToServer(self):  #
        global username
        text =  str(self.input.text())
        self.input.setText('')
        if text == 'Exit' or text=='':
            self.exit()
        try:
            s.send(text.encode('utf-8'))
            print('%s >> %s' % (username, text))
            self.messages.append(self.Nickname+" : " + text )
        except ConnectionAbortedError:
            print('Server closed this connection!')
            self.exit()
        except ConnectionResetError:
            print('Server is closed!')
            self.exit()

    def recvFromServer(self):  #
        while 1:
            try:
                data = s.recv(1024).decode('utf-8')
                if not data:
                    exit()
                print(data)
                self.messages.append(data)
            except ConnectionAbortedError:
                print('Server closed this connection!')
                self.exit()
            except ConnectionResetError:
                print('Server is closed!')
                self.exit()

    def showChat(self):    #
        for m in self.messages:
            self.chat.append(m)
        self.messages = []


    def exit(self):   #
        s.close()
        sys.exit()

    def build(self):
        self.layout.addWidget(self.chat, 0, 0, 5, 4)
        self.layout.addWidget(self.input, 5, 0, 1, 3)
        self.layout.addWidget(self.btnSend, 5, 3)
        self.setLayout(self.layout)


    def createAction(self):
        self.btnSend.clicked.connect(self.sendToServer)
        self.timer.timeout.connect(self.showChat)
        self.timer.start(1000)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

address = ('127.0.0.1', 31500)
Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Sock.sendto(b'1',address)

print(s.recv(1024).decode())

app = QApplication(sys.argv)
log = Log(s)
app.exec_()

#10/4 实现socket通行
#10/6 实现pyqt5封装,界面优化
#10/9 实现udp通信

#made by 12Dong