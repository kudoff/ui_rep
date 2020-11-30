import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.run)
        self.ellipse = False

    def run(self):
        self.ellipse = True
        self.update()

    def paintEvent(self, event):
        QMainWindow.paintEvent(self, event)
        if self.ellipse:
            painter = QPainter(self)
            brush = QBrush(Qt.yellow)
            painter.setBrush(brush)
            size = self.size()
            x, y = randint(1, size.height()), randint(1, size.width())
            r = randint(1, 100)
            painter.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
