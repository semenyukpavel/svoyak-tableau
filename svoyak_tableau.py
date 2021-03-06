#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QErrorMessage, QLabel, QPushButton, QGridLayout, QApplication,\
    QWidget


class SvoyakTableau(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Игроки", "Введите игроков через запятую:", QLineEdit.Normal, "")
        if okPressed:
            return text

    def initUI(self):

        while True:
            player_names = list(map(str.strip, self.getText().split(',')))
            if len(player_names) == 4:
                break
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Количество игроков не равно 4, введите заново')

        theme_num = 5
        # TODO сделать переменное количество игр

        self.themes = ['Тема ' + str(i+1) for i in range(theme_num)]
        self.quests = ['10', '20', '30', '40', '50']

        self.p1 = QLabel(self)
        self.p2 = QLabel(self)
        self.p3 = QLabel(self)
        self.p4 = QLabel(self)

        for name in player_names:
            name.strip()

        self.p1.setText(player_names[0])
        self.p2.setText(player_names[1])
        self.p3.setText(player_names[2])
        self.p4.setText(player_names[3])

        self.players_numbers = {player_names[0]: '1', player_names[1]: '2', player_names[2]: '3', player_names[3]: '4'}
        # TODO намаппить имена с кнопками

        btn_plus_p1 = QPushButton(player_names[0] + ' +', self)
        btn_plus_p2 = QPushButton(player_names[1] + ' +', self)
        btn_plus_p3 = QPushButton(player_names[2] + ' +', self)
        btn_plus_p4 = QPushButton(player_names[3] + ' +', self)
        btn_minus_p1 = QPushButton(player_names[0] + ' -', self)
        btn_minus_p2 = QPushButton(player_names[1] + ' -', self)
        btn_minus_p3 = QPushButton(player_names[2] + ' -', self)
        btn_minus_p4 = QPushButton(player_names[3] + ' -', self)

        self.pts1 = QLabel(self)
        self.pts2 = QLabel(self)
        self.pts3 = QLabel(self)
        self.pts4 = QLabel(self)

        self.pts1.setText('0')
        self.pts2.setText('0')
        self.pts3.setText('0')
        self.pts4.setText('0')

        self.themeN = QLabel(self)
        self.questN = QLabel(self)

        self.theme_num = 0
        self.quest_num = 0

        self.themeN.setText(self.themes[self.theme_num])
        self.questN.setText(self.quests[self.quest_num])

        next_q_btn = QPushButton('Следующий вопрос', self)

        btn_plus_p1.clicked.connect(self.buttonClicked)
        btn_plus_p2.clicked.connect(self.buttonClicked)
        btn_plus_p3.clicked.connect(self.buttonClicked)
        btn_plus_p4.clicked.connect(self.buttonClicked)
        btn_minus_p1.clicked.connect(self.buttonClicked)
        btn_minus_p2.clicked.connect(self.buttonClicked)
        btn_minus_p3.clicked.connect(self.buttonClicked)
        btn_minus_p4.clicked.connect(self.buttonClicked)

        next_q_btn.clicked.connect(self.qButtonClicked)

        widgets = [self.p1, self.p2, self.p3, self.p4, self.pts1, self.pts2,
                   self.pts3, self.pts4, self.themeN, self.questN, btn_plus_p1,
                   btn_plus_p2, btn_plus_p3, btn_plus_p4, btn_minus_p1,
                   btn_minus_p2, btn_minus_p3, btn_minus_p4, next_q_btn]

        for widget in widgets:
            widget.resize(widget.sizeHint())
            if widget in [self.p1, self.p2, self.p3, self.p4, self.themeN,
                          self.questN, self.pts1, self.pts2,
                          self.pts3, self.pts4]:
                widget.setAlignment(Qt.AlignCenter)

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.p1, 0, 0)
        grid.addWidget(self.p2, 0, 1)
        grid.addWidget(self.p3, 0, 3)
        grid.addWidget(self.p4, 0, 4)
        grid.addWidget(self.pts1, 1, 0)
        grid.addWidget(self.pts2, 1, 1)
        grid.addWidget(self.themeN, 1, 2)
        grid.addWidget(self.pts3, 1, 3)
        grid.addWidget(self.pts4, 1, 4)
        grid.addWidget(btn_plus_p1, 2, 0)
        grid.addWidget(btn_plus_p2, 2, 1)
        grid.addWidget(self.questN, 2, 2)
        grid.addWidget(btn_plus_p3, 2, 3)
        grid.addWidget(btn_plus_p4, 2, 4)
        grid.addWidget(btn_minus_p1, 3, 0)
        grid.addWidget(btn_minus_p2, 3, 1)
        grid.addWidget(next_q_btn, 3, 2)
        grid.addWidget(btn_minus_p3, 3, 3)
        grid.addWidget(btn_minus_p4, 3, 4)

        self.setGeometry(200, 200, 900, 500)
        self.setWindowTitle('Табло для Своей игры')
        self.show()

    def buttonClicked(self):
        sender_txt = self.sender().text()
        print(sender_txt)
        sender_name = sender_txt.split(' ')[0] + ' ' + sender_txt.split(' ')[1]
        if sender_txt[-1] == '+':
            if self.players_numbers[sender_name] == '1':
                res = int(self.pts1.text())
                self.pts1.setText(str(res + int(self.questN.text())))
                self.pts1.repaint()
            elif self.players_numbers[sender_name] == '2':
                res = int(self.pts2.text())
                self.pts2.setText(str(res + int(self.questN.text())))
                self.pts2.repaint()
            elif self.players_numbers[sender_name] == '3':
                res = int(self.pts3.text())
                self.pts3.setText(str(res + int(self.questN.text())))
                self.pts3.repaint()
            elif self.players_numbers[sender_name] == '4':
                res = int(self.pts4.text())
                self.pts4.setText(str(res + int(self.questN.text())))
                self.pts4.repaint()
        elif sender_txt[-1] == '-':
            if self.players_numbers[sender_name] == '1':
                res = int(self.pts1.text())
                self.pts1.setText(str(res - int(self.questN.text())))
                self.pts1.repaint()
            elif self.players_numbers[sender_name] == '2':
                res = int(self.pts2.text())
                self.pts2.setText(str(res - int(self.questN.text())))
                self.pts2.repaint()
            elif self.players_numbers[sender_name] == '3':
                res = int(self.pts3.text())
                self.pts3.setText(str(res - int(self.questN.text())))
                self.pts3.repaint()
            elif self.players_numbers[sender_name] == '4':
                res = int(self.pts4.text())
                self.pts4.setText(str(res - int(self.questN.text())))
                self.pts4.repaint()

    def qButtonClicked(self):
        if self.quest_num < 4:
            self.quest_num += 1
            self.questN.setText(self.quests[self.quest_num])
            self.questN.repaint()
        elif self.theme_num < 4:
            self.theme_num += 1
            self.quest_num -= 4
            self.themeN.setText(self.themes[self.theme_num])
            self.questN.setText(self.quests[self.quest_num])
            self.questN.repaint()
            self.themeN.repaint()
        else:
            self.themeN.setText('Тема 0')
            self.questN.setText('0')
            self.questN.repaint()
            self.themeN.repaint()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    st = SvoyakTableau()
    sys.exit(app.exec_())