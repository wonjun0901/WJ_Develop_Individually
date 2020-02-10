import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from widgetfor_start import *
from menu import *


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.menus = self.menuBar()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Program for QuadMedicine')
        self.setGeometry(300, 100, 800, 800)
        self.statusBar().showMessage('Ready', 5000)

        #self.actions = action1()
        widget1 = WidgetinMainwindow()
        menu = menubar_main()

        self.setCentralWidget(widget1)
        self.setMenuBar(menu)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
