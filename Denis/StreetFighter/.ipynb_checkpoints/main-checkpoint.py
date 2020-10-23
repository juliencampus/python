# importations à faire pour la réalisation d'une interface graphique

import players
import threading

import time
import sys
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QTransform, QPainter, QColor, QFont
from PyQt5.QtMultimedia import QSound


class Fenetre(QWidget):
    def __init__(self, sound, player):
        QWidget.__init__(self)
        self.setWindowTitle("Street Fighter")
        self.sound = sound
        self.state = 0
        self.player = player
        self.ennemi = players.Player("assets/ken_normal_left.png", "assets/ken_fight_left.png")
        self.playSound("assets/sounds/title.wav")
        self.resize(1200, 1000)
        self.label = QLabel(self)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.state != 1:
            self.game()
        elif event.button() == Qt.RightButton:
            print("Appui bouton droite")

    def keyPressEvent(self, event):
        if self.state == 1:
            if event.key() == Qt.Key_Right and player.x < self.width() - 200:
                self.player.x += 20
                self.update()

            elif event.key() == Qt.Key_Left and player.x > 10:
                self.player.x -= 20
                self.update()

            elif event.key() == Qt.Key_Space:
                self.player.fight(self.ennemi)
                self.playSound("assets/sounds/punch.wav")
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


    def showPlayer(self, player):
        label = QPainter(self)
        label.begin(self)
        pixmap = QImage(player.picFight if player.isFight else player.picNormally)
        label.drawImage(player.x, player.y, pixmap)

    def drawLife(self):
        # Player :
        painter = QPainter(self)
        painter.begin(self)
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(8, 100, round((self.width() / 2) - 20), 20)

        painterLife = QPainter(self)
        painterLife.begin(self)
        painterLife.setBrush(QColor(255, 255, 0))
        percentLife = self.player.life / 200
        painterLife.drawRect(9, 101, round((self.width() / 2 - 20) * percentLife), 18)

        # Ennemi :
        painterEnnemi = QPainter(self)
        painterEnnemi.begin(self)
        painterEnnemi.setBrush(QColor(255, 0, 0))
        painterEnnemi.drawRect(round(self.width() / 2 + 30), 100, round((self.width() / 2) - 40), 20)

        painterLifeEnnemi = QPainter(self)
        painterLifeEnnemi.begin(self)
        painterLifeEnnemi.setBrush(QColor(255, 255, 0))
        percentLifeEnnemi = self.ennemi.life / 200
        painterLifeEnnemi.drawRect(round(self.width() / 2 + 31), 101, round((self.width() / 2 - 40) * percentLifeEnnemi), 18)



    def paintEvent(self, event):
        if self.state == 1:
            self.showPlayer(self.player)
            self.showPlayer(self.ennemi)
            self.drawLife()
            if self.player.life <= 0:
                self.playSound("assets/sounds/combat.wav", False)
                self.playSound("assets/sounds/youlose.wav")
                self.drawLose()
                self.state = 2
            if self.ennemi.life <= 0:
                self.playSound("assets/sounds/combat.wav", False)
                self.playSound("assets/sounds/youwin.wav")
                self.drawWin()
                self.state = 3
        elif self.state == 2:
            print("U lose")
            self.drawLose()
            self.update()
        elif self.state == 3:
            print("U Win")
            self.drawWin()
            self.update()

    def drawLose(self):
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        painter = QPainter(self)
        painter.setFont(font)
        painter.setPen(QColor(247, 76, 16))
        painter.drawText(self.width() / 2 - 100, 200, "You Loose !")

    def drawWin(self):
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        painter = QPainter(self)
        painter.setFont(font)
        painter.setPen(QColor(247, 76, 16))
        painter.drawText(self.width() / 2 - 100, 200, "You Win !")


    def playSound(self, url, play=True):
        if play:
            self.sound.play(url)
        else:
            self.sound.stop()

    def game(self):
        self.playSound("assets/sounds/combat.wav")
        self.changeBack("assets/fond.jpg")
        self.state = 1
        self.player.x = 20
        self.player.life = 200
        self.showPlayer(self.player)
        self.ennemi.x = self.width() - 200
        self.showPlayer(self.ennemi)


def mainTitle(fen):
    fen.changeBack("assets/start.png")

def sync(f_stop, player):
    if not f_stop.is_set():
        player.isFight = False
        threading.Timer(1, sync, [f_stop, player]).start()

app = QApplication(sys.argv)

# création d'une fenêtre avec QWidget dont on place la référence dans fen

sound = QSound("")

# la fenêtre est rendue visible

# fen.playSound("assets/sounds/title.wav")

player = players.Player("assets/ryu_normal.png", "assets/ryu_fight.png")

f_stop = threading.Event()
sync(f_stop, player)
fen = Fenetre(sound, player)
fen.show()
mainTitle(fen)
# fen.showPlayer(player, player.x, player.y)

# exécution de l'application, l'exécution permet de gérer les événements
app.exec_()

