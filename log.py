import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLineEdit,QTextEdit,QLabel,QPushButton,QFrame,QHBoxLayout,QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon


class Log(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

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
        print(name)
        self.close()
    def creationAction(self):
        self.btnStart.clicked.connect(self.setNickname)
if __name__=="__main__":
    app = QApplication(sys.argv)
    exp = Log()
    app.exec_()