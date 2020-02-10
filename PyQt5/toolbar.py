import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon

# 메뉴(menu)가 어플리케이션에서 사용되는 모든 명령의 모음이라면, 툴바(toolbar)는 자주 사용하는 명령들을 더 편리하게 사용할 수 있도록 해줍니다.


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 메뉴바의 경우와 마찬가지로 QAction 객체를 하나 생성합니다.
        # 이 객체는 아이콘(exit.png), 라벨('Exit')을 포함하고, 단축키(Ctrl+Q)를 통해 실행 가능합니다.
        # 상태바에 메세지('Exit application')를 보여주고 클릭 시 생성되는 시그널은
        # quit() 메소드에 연결되어 있습니다.
        exitAction = QAction(QIcon('PyQt5/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # 다음 두줄을 통하여 툴바를 만들고 툴바에 exitAction 동작을 추가했습니다.
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)

        # 창을 화면의 가운데로 하는 일은 center() 메소드를 통해 수행됩니다.
        self.center()
        self.show()

    def center(self):

        # frameGeometry() 메소드를 이용해서 창의 위치와 크기 정보를 가져옵니다.
        qr = self.frameGeometry()

        # 사용하는 모니터 화면의 가운데 위치를 파악합니다.
        cp = QDesktopWidget().availableGeometry().center()

        # 창의 직사각형 위치를 화면의 중심위치로 이동합니다.
        qr.moveCenter(cp)

        # 현재 창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.
        # 결과적으로 현재 창의 중심이 화면의 중심과 일치하게 되서 창이 가운데에 나타나게 됩니다.
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
