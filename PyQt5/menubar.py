import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

# 메인창(Main Window)은 메뉴바, 툴바, 상태바를 갖는 전형적인 어플리케이션 창입니다.
# 메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 레이아웃을 가지고 있습니다.
# 또한 가운데 영역에 중심위젯(Central Widget)을 위한 영역을 갖고 있습니다. 여기에는 어떠한 위젯도 들어올 수 있습니다

# QMainWindow 클래스를 이용하여 메인 어플리케이션 창을 만들 수 있습니다.

# 우선 QStatusBar를 이용해서 메인 창에 상태바를 하나 만들어보겠습니다.
# 상태바는 어플리케이션 상태를 알려주기 위해 어플리케이션의 하단에 위치하는 위젯입니다.

# 상태바에 텍스트를 표시하기 위해서는 showMessage() 메소드를 사용합니다.
# 텍스트가 사라지게 하고 싶으면 clearMessage() 메소드를 사용하거나
# showMessage() 메소드에 텍스트가 표시되는 시간을 설정할 수 있습니다.

# 현재 상태바에 표시되는 메세지 텍스트를 갖고 오고 싶을 때는 currentMessage() 메소드를 사용합니다.
# QStatusBar 클래스는 상태바에 표시되는 메세지가 바뀔 때마다 messageChanged() 시그널을 발생합니다.

##############################################################################################

# GUI 어플리케이션에서 메뉴바(menu bar)는 흔하게 사용됩니다. 다양한 명령들의 모음이 메뉴바에 위치합니다.


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 상태바는 QMainWindow 클래스의 statusBar() 메소드를 이용해서 만드는데 statusBar() 메소드를 최초로 호출함으로써 만들어집니다.
        # 그 다음 호출부터는 상태바 객체를 반환합니다.
        self.statusBar().showMessage('Ready', 5000)

        # 다음의 4줄 코드를 통해 아이콘(exit.png)과 'Exit!!!!!' 라벨을 갖는 하나의 동작(action)을 만들고
        # 이 동작에 대한 단축키(setShortcut)를 정의합니다.
        # 또한 메뉴에서 마우스를 올렸을 때, 상태바에 나타날 상태팁을 setStatusTip() 메소드를 사용해서 설정했습니다.
        exitAction = QAction(QIcon('PyQt5/exit.png'), 'Exit!!!!!', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을 때, 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 어플리케이션을 종료시키게 됩니다.
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # menuBar() 메소드는 메뉴바를 생성합니다. 이어서 'File' 메뉴를 하나 만들고, 거기에 'exitAction' 동작을 추가합니다.
        # '&File'의 앰퍼샌드(ampersand, &)는 간편하게 단축키를 설정하도록 해줍니다.
        # 'F' 앞에 앰퍼샌드가 있으므로 'Alt + F'가 File 메뉴의 단축키가 됩니다. 만약 'i'의 앞에 앰퍼샌드를 넣으면 'alt + i' 가 단축키가 됩니다.
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')

        fileMenu.addAction(exitAction)
        editMenu = menubar.addMenu('&Edit')

        self.setWindowTitle('Status Bar')
        self.setGeometry(300, 300, 300, 200)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
