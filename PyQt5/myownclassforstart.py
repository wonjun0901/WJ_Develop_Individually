import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class action1(QAction):

    def initUI(self):

        # 상태바는 QMainWindow 클래스의 statusBar() 메소드를 이용해서 만드는데 statusBar() 메소드를 최초로 호출함으로써 만들어집니다.
        # 그 다음 호출부터는 상태바 객체를 반환합니다.
        # self.statusBar().showMessage('Ready', 5000)

        # 다음의 4줄 코드를 통해 아이콘(exit.png)과 'Exit!!!!!' 라벨을 갖는 하나의 동작(action)을 만들고
        # 이 동작에 대한 단축키(setShortcut)를 정의합니다.
        # 또한 메뉴에서 마우스를 올렸을 때, 상태바에 나타날 상태팁을 setStatusTip() 메소드를 사용해서 설정했습니다.
        exitAction = QAction(QIcon('PyQt5/exit.png'), 'E&xit', self)
        exitAction.setShortcut('q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction(QIcon('PyQt5/save.png'), 'Save', self)
        saveAction.setShortcut('s')
        saveAction.setStatusTip('Save the result')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        # saveAction.triggered.connect(qApp.quit)

        printAction = QAction(QIcon('PyQt5/print.png'), 'Print', self)
        printAction.setShortcut('p')
        printAction.setStatusTip('Print application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        # printAction.triggered.connect(qApp.quit)

        list_1 = [saveAction, printAction, exitAction]

        # self.statusBar()
        return list_1


class action2(QAction):
    def initUI(self):
        exitAction = QAction(QIcon('PyQt5/exit.png'), '&Exit!!!!!', self)
        # exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        exitAction = QAction(QIcon('PyQt5/exit.png'), 'Exit!!!!!', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        exitAction = QAction(QIcon('PyQt5/exit.png'), 'Exit!!!!!', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        exitAction = QAction(QIcon('PyQt5/exit.png'), 'Exit!!!!!', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        exitAction = QAction(QIcon('PyQt5/exit.png'), 'Exit!!!!!', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        exitAction = QAction(QIcon('PyQt5/exit.png'), 'Exit!!!!!', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        exitAction = QAction(QIcon('PyQt5/exit.png'), 'Exit!!!!!', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)
