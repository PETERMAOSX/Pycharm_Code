import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('test_2.png'))
        self.show()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())