import players

import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from PyQt5.QtMultimedia import QSound

app = QApplication(sys.argv)

sound = QSound("assets/sounds/title.wav")
sound.play()

app.exec_()