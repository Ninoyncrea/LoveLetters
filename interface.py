import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFrame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QToolButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Window(QWidget):

    def __init__(self, win):
        super().__init__()
        self.window = win
        self.dico = {"J0": "comptesse","J1":"roi","J2":"garde","J3":"baron"}
        self.pioche = "servante"
        self.nom_joueur = "J0"
        #self.nbre_joueurs = 3


    def action1(self):
        appareillage = {"garde":"1","prêtre":"2","baron":"3","servante":"4","prince":"5","roi":"6","comptesse":"7","princesse":"8"}
        url_next_card = "carte"+appareillage.get(self.pioche)+".jpg"
        self.button1.setStyleSheet("QPushButton { background-image: url("+url_next_card+"); }")

    def action2(self):
        appareillage = {"garde":"1","prêtre":"2","baron":"3","servante":"4","prince":"5","roi":"6","comptesse":"7","princesse":"8"}
        url_next_card = "carte"+appareillage.get(self.pioche)+".jpg"
        self.button2.setStyleSheet("QPushButton { background-image: url("+url_next_card+"); }")

    def buildWindow(self, win):

        win.setGeometry(0, 0, 100000, 1000000)
        self.frame = QFrame(win)
        self.width_win = 1950
        self.height_win = 1000
        self.width_card = 260
        self.height_card = 351
        self.frame.setGeometry(0, 0, self.width_win, self.height_win)

        self.grid = QGridLayout()
        self.frame.setLayout(self.grid)

        background = QLabel(self)
        pixmap = QPixmap('taverne.jpg')
        background.setPixmap(pixmap)
        background.setFixedSize(pixmap.width(), pixmap.height())
        self.grid.addWidget(background)

        self.button1 = QPushButton(win)
        self.grid.addWidget(self.button1, 0, 0)
        self.button1.setStyleSheet("QPushButton { background-image: url('carte1.jpg'); }")
        self.button1.setFixedSize(self.width_card, self.height_card)
        self.grid.setAlignment(self.button1, Qt.AlignLeft)
        self.button1.clicked.connect(self.action1)

        self.button2 = QPushButton(win)
        self.grid.addWidget(self.button2, 0, 1)
        self.button2.setStyleSheet("QPushButton { background-image: url('carte2.jpg'); }")
        self.button2.setFixedSize(self.width_card, self.height_card)
        self.grid.setAlignment(self.button2, Qt.AlignRight)
        self.button2.clicked.connect(self.action2)

        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 1)

    def choixJoueurs(self, button):

        if button == self.button1:
            self.nombre_joueurs = 1
            self.launchNewWindow()

        elif button == self.button2:
            self.nombre_joueurs = 2

        elif button == self.button3:
            self.nombre_joueurs = 3

        elif button == self.button4:
            self.nombre_joueurs = 4

        button.setText("nombre joueurs  = " + str(self.nombre_joueurs))

    def buildWindowInit(self,win):

        nombre_joueurs =0

        win.setGeometry(0, 0, 100000, 1000000)
        self.frame = QFrame(win)
        self.width_win = 1950
        self.height_win = 1000
        self.width_card = 260
        self.height_card = 351
        self.frame.setGeometry(0, 0, self.width_win, self.height_win)

        self.grid = QGridLayout()
        self.frame.setLayout(self.grid)

        background = QLabel(self)
        pixmap = QPixmap('carte6.jpg')
        background.setPixmap(pixmap)
        background.setFixedSize(pixmap.width(), pixmap.height())
        self.grid.addWidget(background)

        self.button1 = QPushButton(win)
        self.button1.setText("Button 1")
        self.grid.addWidget(self.button1, 0, 0)
        self.button1.clicked.connect(lambda: self.choixJoueurs(self.button1))

        self.button2 = QPushButton(win)
        self.button2.setText("Button 2")
        self.grid.addWidget(self.button2, 1, 0)
        self.button2.clicked.connect(lambda: self.choixJoueurs(self.button2))

        self.button3 = QPushButton(win)
        self.button3.setText("Button 3")
        self.grid.addWidget(self.button3, 0, 1)
        self.button3.clicked.connect(lambda: self.choixJoueurs(self.button3))

        self.button4 = QPushButton(win)
        self.button4.setText("Button 4")
        self.grid.addWidget(self.button4, 1, 1)
        self.button4.clicked.connect(lambda: self.choixJoueurs(self.button4))

        return nombre_joueurs


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    myWindow = Window(win)
    myWindow.buildWindowInit(win)
    win.show()
    app.exec_()

