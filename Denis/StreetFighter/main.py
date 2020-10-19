# importations à faire pour la réalisation d'une interface graphique

import players

import time
import sys
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QTransform, QPainter
from PyQt5.QtMultimedia import QSound

game = 0

class Fenetre(QWidget):
    def __init__(self, sound):
        QWidget.__init__(self)
        self.setWindowTitle("Street Fighter")
        self.sound = sound
        self.sate = 0
        self.player = players.Player("assets/ryu_normal.png", "assets/ryu_fight.png")
        self.ennemi = players.Player("assets/ken_normal_left.png", "assets/ken_fight_left.png")
        self.playSound("assets/sounds/title.wav")
        self.resize(1200, 1000)
        self.label = QLabel(self)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.playSound("assets/sounds/combat.wav")
            self.changeBack("assets/fond.jpg")
            self.game()
        elif event.button() == Qt.RightButton:
            print("Appui bouton droite")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.player.isFight = False
            self.player.x += 20
            self.update()

        elif event.key() == Qt.Key_Left:
            self.player.isFight = False
            self.player.x -= 20
            self.update()

        elif event.key() == Qt.Key_Space:
            self.player.isFight = True
            self.update()

        # elif event.key() == Qt.Key_Up:
        #     self.player.y -= 60
        #     self.update()


    def changeBack(self, pic):
        oImage = QImage(pic)
        sImage = oImage.scaled(self.width(), self.height())  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)


    def showPlayer(self, player, fight=False, rotate=False):
        label = QPainter(self)
        label.begin(self)
        pixmap = QImage(player.picFight if fight else player.picNormally)
        # label.setGeometry(player.x, player.y, player.width, player.height)
        label.drawImage(player.x, player.y, pixmap)


    def paintEvent(self, event):
        print(event)
        self.showPlayer(self.player, self.player.isFight)
        self.showPlayer(self.ennemi)



    def playSound(self, url, play=True):
        if play:
            self.sound.play(url)
        else:
            self.sound.stop()

    def game(self):
        self.showPlayer(self.player)
        self.ennemi.x = self.width() - 200
        self.showPlayer(self.ennemi, False, True)


def mainTitle(fen):
    fen.changeBack("assets/start.png")


app = QApplication(sys.argv)

# création d'une fenêtre avec QWidget dont on place la référence dans fen

sound = QSound("")
fen = Fenetre(sound)

# la fenêtre est rendue visible
fen.show()
# fen.playSound("assets/sounds/title.wav")

mainTitle(fen)

player = players.Player("assets/ryu_normal.png", "assets/ryu_fight.png")

# fen.showPlayer(player, player.x, player.y)

# exécution de l'application, l'exécution permet de gérer les événements
app.exec_()

