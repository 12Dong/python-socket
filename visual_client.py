# coding:utf-8

import socket
import threading
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLineEdit,QTextEdit,QLabel,QPushButton
from PyQt5 import QtCore,QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import*
from PyQt5.QtGui import QIcon

host = 'localhost'
port = 10000
username = '12Dong'


class Client(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Client')
        self.setNameWidget = QWidget()#
        self.layout = QGridLayout(self)#
        self.setNameLayout = QGridLayout(self.setNameWidget)#
        self.btnSend = QPushButton('send')#
        self.btnSet = QPushButton('Set')#
        self.input = QLineEdit()#
        self.name = QLineEdit('Default')#
        self.chat = QTextEdit()#
        self.label = QLabel('name:')#

        self.timer = QtCore.QTimer()
        self.messages = []

        self.build()
        self.createAction()
        self.setWindowIcon(QIcon("mylove.ico"))

        recvThread = threading.Thread(target=self.recvFromServer) #
        recvThread.start()#

        self.setGeometry(500,500,600,400)
        self.setWindowTitle('Communcation')

    def sendToServer(self):  #
        global username
        text =  str(self.input.text())
        self.input.setText('')
        if text == 'Exit' or text=='':
            self.exit()
        try:
            s.send(('%s: %s' % (username, text)).encode('utf-8'))
            print('%s >> %s' % (username, text))
            self.messages.append(username+ " : " + text )
        except:
            self.exit()

    def recvFromServer(self):  #
        while 1:
            try:
                data = s.recv(1024).decode('utf-8')
                if not data:
                    exit()
                print("Server :" + data)
                self.messages.append("Server "+" : "+data)
            except:
                return

    def showChat(self):    #
        for m in self.messages:
            self.chat.append(m)
        self.messages = []

    def slotExtension(self):#
        global username
        name = str(self.name.text())
        if name.strip() != '':
            username = name
            print(name)

    def exit(self):   #
        s.close()
        sys.exit()

    def build(self):
        self.layout.addWidget(self.chat, 0, 0, 5, 4)
        self.layout.addWidget(self.input, 5, 0, 1, 4)
        self.layout.addWidget(self.btnSend, 5, 4)

        self.setNameLayout.addWidget(self.label, 0, 0)
        self.setNameLayout.addWidget(self.name, 0, 1)
        self.setNameLayout.addWidget(self.btnSet, 0, 4)
        self.layout.addWidget(self.setNameWidget, 6, 0)
        self.setLayout(self.layout)


    def createAction(self):
        self.btnSend.clicked.connect(self.sendToServer)
        self.btnSet.clicked.connect(self.slotExtension)
        self.timer.timeout.connect(self.showChat)
        self.timer.start(1000)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(username.encode('utf-8'))
print(username + " is connected ")

app = QApplication(sys.argv)
c = Client()
c.show()
app.exec_()

#10/4 实现socket通行
#10/6 实现pyqt5封装