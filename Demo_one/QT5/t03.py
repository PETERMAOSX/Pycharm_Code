import sys
from PyQt5.QtWidgets import (QWidget,QToolTip,QPushButton,QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont("SansSerif",10))
        self.setToolTip("This is a <b>QWidget</b> widget")
        btn = QPushButton('Button',self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        self.setGeometry(640,480,300,300)
        self.setWindowTitle("Perter Mao")
        self.show()

app = QApplication(sys.argv)
example = Example()
sys.exit(app.exec_())