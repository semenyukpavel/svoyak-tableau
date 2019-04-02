#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber


class SvoyakTableau(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn_plus_p1 = QPushButton('Игрок 1 +', self)
        btn_plus_p2 = QPushButton('Игрок 2 +', self)
        btn_plus_p3 = QPushButton('Игрок 3 +', self)
        btn_plus_p4 = QPushButton('Игрок 4 +', self)
        btn_minus_p1 = QPushButton('Игрок 1 -', self)
        btn_minus_p2 = QPushButton('Игрок 2 -', self)
        btn_minus_p3 = QPushButton('Игрок 3 -', self)
        btn_minus_p4 = QPushButton('Игрок 4 -', self)

        btn_plus_p1.move(100, 300)
        btn_plus_p2.move(250, 300)
        btn_plus_p3.move(550, 300)
        btn_plus_p4.move(700, 300)
        btn_minus_p1.move(100, 450)
        btn_minus_p2.move(250, 450)
        btn_minus_p3.move(550, 450)
        btn_minus_p4.move(700, 450)

        self.pts1 = QLCDNumber(self)
        self.pts2 = QLCDNumber(self)
        self.pts3 = QLCDNumber(self)
        self.pts4 = QLCDNumber(self)

        self.pts1.setMinimumSize(100, 50)
        self.pts2.setMinimumSize(100, 50)
        self.pts3.setMinimumSize(100, 50)
        self.pts4.setMinimumSize(100, 50)

        self.pts1.move(100, 150)
        self.pts2.move(250, 150)
        self.pts3.move(550, 150)
        self.pts4.move(700, 150)

        btn_plus_p1.clicked.connect(self.buttonClicked)
        btn_plus_p2.clicked.connect(self.buttonClicked)
        btn_plus_p3.clicked.connect(self.buttonClicked)
        btn_plus_p4.clicked.connect(self.buttonClicked)
        btn_minus_p1.clicked.connect(self.buttonClicked)
        btn_minus_p2.clicked.connect(self.buttonClicked)
        btn_minus_p3.clicked.connect(self.buttonClicked)
        btn_minus_p4.clicked.connect(self.buttonClicked)

        self.setGeometry(200, 200, 900, 500)
        self.setWindowTitle('Табло для Своей игры')
        self.show()

    def buttonClicked(self):
        sender_txt = self.sender().text()
        if sender_txt[-1] == '+':
            if sender_txt[-3] == '1':
                res = self.pts1.intValue()
                self.pts1.display(res + 10)
                self.pts1.repaint()
            elif sender_txt[-3] == '2':
                res = self.pts2.intValue()
                self.pts2.display(res + 10)
                self.pts2.repaint()
            elif sender_txt[-3] == '3':
                res = self.pts3.intValue()
                self.pts3.display(res + 10)
                self.pts3.repaint()
            elif sender_txt[-3] == '4':
                res = self.pts4.intValue()
                self.pts4.display(res + 10)
                self.pts4.repaint()
        elif sender_txt[-1] == '-':
            if sender_txt[-3] == '1':
                res = self.pts1.intValue()
                self.pts1.display(res - 10)
                self.pts1.repaint()
            elif sender_txt[-3] == '2':
                res = self.pts2.intValue()
                self.pts2.display(res - 10)
                self.pts2.repaint()
            elif sender_txt[-3] == '3':
                res = self.pts3.intValue()
                self.pts3.display(res - 10)
                self.pts3.repaint()
            elif sender_txt[-3] == '4':
                res = self.pts4.intValue()
                self.pts4.display(res - 10)
                self.pts4.repaint()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    st = SvoyakTableau()
    sys.exit(app.exec_())
