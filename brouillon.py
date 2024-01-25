import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFrame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QToolButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

class Window(QWidget):

    def __init__(self, win):
        super().__init__()
        self.window = win
        self.secondary_window = win
        self.dico = {"J0": "comptesse", "J1": "roi", "J2": "garde", "J3": "baron"}
        self.pioche = "servante"
        self.nom_joueur = "J0"
        # self.nbre_joueurs = 3

    def action1(self):
        appareillage = {"garde":"1","prêtre":"2","baron":"3","servante":"4","prince":"5","roi":"6","comptesse":"7","princesse":"8"}
        url_next_card = "carte"+appareillage.get(self.pioche)+".jpg"
        self.button1.setStyleSheet("QPushButton { background-image: url("+url_next_card+"); }")

    def action2(self):
        appareillage = {"garde":"1","prêtre":"2","baron":"3","servante":"4","prince":"5","roi":"6","comptesse":"7","princesse":"8"}
        url_next_card = "carte"+appareillage.get(self.pioche)+".jpg"
        self.button2.setStyleSheet("QPushButton { background-image: url("+url_next_card+"); }")

    def secondaryWindow(self, win):

        win.setGeometry(0, 0, 100000, 1000000)
        self.secondary_window.frame = QFrame(win)
        self.secondary_window.width_win = 1950
        self.secondary_window.height_win = 1000
        self.secondary_window.width_card = 260
        self.secondary_window.height_card = 351
        self.secondary_window.frame.setGeometry(0, 0, self.secondary_window.width_win, self.secondary_window.height_win)

        self.secondary_window.grid = QGridLayout()
        self.secondary_window.frame.setLayout(self.secondary_window.grid)

        background = QLabel(self.secondary_window)
        pixmap = QPixmap('taverne.jpg')
        background.setPixmap(pixmap)
        background.setFixedSize(pixmap.width(), pixmap.height())
        self.secondary_window.grid.addWidget(background)

        self.secondary_window.button1 = QPushButton(win)
        self.secondary_window.grid.addWidget(self.secondary_window.button1, 0, 0)
        self.secondary_window.button1.setStyleSheet("QPushButton { background-image: url('carte1.jpg'); }")
        self.secondary_window.button1.setFixedSize(self.secondary_window.width_card, self.secondary_window.height_card)
        self.secondary_window.grid.setAlignment(self.secondary_window.button1, Qt.AlignLeft)
        self.secondary_window.button1.clicked.connect(self.action1)

        self.secondary_window.button2 = QPushButton(win)
        self.secondary_window.grid.addWidget(self.secondary_window.button2, 0, 0)
        self.secondary_window.button2.setStyleSheet("QPushButton { background-image: url('carte2.jpg'); }")
        self.secondary_window.button2.setFixedSize(self.secondary_window.width_card, self.secondary_window.height_card)
        self.secondary_window.grid.setAlignment(self.secondary_window.button1, Qt.AlignLeft)
        self.secondary_window.button2.clicked.connect(self.action2)

        self.secondary_window.grid.setColumnStretch(0, 1)
        self.secondary_window.grid.setColumnStretch(1, 1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    myWindow = Window(win)
    myWindow.secondaryWindow(win)
    win.show()
    app.exec_()