import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Hello Peter")
w.resize(640,480)
w.move(300,300)
w.show()
sys.exit(app.exec_())