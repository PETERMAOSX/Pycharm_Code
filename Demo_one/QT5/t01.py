import sys
from PyQt5.QtWidgets import QApplication,QWidget
#引入PyQt5.QtWidgets库

app = QApplication(sys.argv) #每一个PyQt5应用都必须创建一个应用对象。
#sys.argv是一组命令行参数的列表。
w = QWidget()  #QWidget是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况先，构造器是没有父级的，没有父级的构造器成为window
w.resize(640,480)  #resize方法可以改变控件的大小，这里的意思是窗口宽250px,高150px
w.move(300,300)  #move是移动控件位置的方法。它把控件放置到屏幕的坐标(300,300)的位置。原点是屏幕的左上角
w.setWindowTitle("Hello PeterMao")  #添加一个标题
w.show()  #让窗口显现出来
sys.exit(app.exec_()) #sys.exit用来确保程序安全退出