#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


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
        btn_plus_p2.move(300, 300)
        btn_plus_p3.move(500, 300)
        btn_plus_p4.move(700, 300)
        btn_minus_p1.move(100, 450)
        btn_minus_p2.move(300, 450)
        btn_minus_p3.move(500, 450)
        btn_minus_p4.move(700, 450)

        self.setGeometry(200, 200, 900, 500)
        self.setWindowTitle('Табло для Своей игры')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    st = SvoyakTableau()
    sys.exit(app.exec_())
