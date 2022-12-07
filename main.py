from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
from random import randint
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.p)
        self.flag = False
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 8))
            painter.drawEllipse(self.x1, self.y1, self.x2, self.y2)

    def p(self):
        self.flag = True
        k = randint(5, 250)
        t = 250 - k
        self.x1 = 250 - t
        self.y1 = 250 - t
        self.x2 = 250 + t
        self.y2 = 250 + t

        self.update()
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
