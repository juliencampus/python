import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from Character import *

class Window(QWidget):
    def __init__(self, teams):
        super().__init__()
        self.teams = teams
        self.button = QPushButton("CLOSE")
        self.button.clicked.connect(self.close_event)
        self.setLayout(QHBoxLayout())
        vlayouts = [QVBoxLayout(), QVBoxLayout()]
        self.layout().addLayout(vlayouts[0])
        self.layout().addLayout(vlayouts[1])
        for i, x in enumerate(self.teams):
            for char in x:
                lbl = QLabel()
                imgsrc = f"assets/{'mage.png' if isinstance(char,Mage) else 'warrior.png' if isinstance(char, Guerrier) else 'archer.png' if isinstance(char, Archer) else 'rip.png'}"
                pix  = QPixmap(imgsrc).scaled(80,80)
                lbl.setPixmap(pix)
                lbl.resize(5, 5)
                vlayouts[i].addWidget(lbl)
        self.layout().addWidget(self.button)
        # self.setLayout(layout)

    def close_event(self, event):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    w = Window([])
    w.show()
    app.exec_()