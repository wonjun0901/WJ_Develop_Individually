import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Icon')

        # setWindowIcon() 메소드는 어플리케이션 아이콘을 설정하도록 합니다.
        # 이를 위해서 QIcon 객체를 생성하였습니다. QIcon()에 보여질 이미지('PyQt5/web.png')를 입력합니다.
        # 이미지 파일을 다른 폴더에 따로 저장해둔 경우에는 경로까지 함께 입력해주시면 됩니다.
        self.setWindowIcon(QIcon('PyQt5/web.png'))

        # setGeometry()메소드는 창의 위치와 크기를 설정합니다. 앞의 두 매개변수는 창의 x, y 위치를 결정하고
        # 뒤의 두 매개변수는 각각 창의 너비와 높이를 결정합니다.
        # 이 메소드는 move()와 resize() 메소드를 하나로 합쳐놓은 것과 동일합니다.
        self.setGeometry(300, 300, 300, 200)

        # 푸시 버튼을 하나 만듭니다. by QPushButton()
        # 이 버튼(btn)은 QPushButton 클래스의 인스턴스입니다.
        # 생성자(QPushButton())의 첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력하고
        # 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력합니다. (여기선 MyApp)
        btn = QPushButton('Quit', self)
        btn.setToolTip('<b>Are you sure to quit this program?</b>')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        # PyQt5에서의 이벤트 처리는 시그널과 슬롯 메커니즘으로 이루어집니다.
        # 버튼을 클릭하면 'clicked' 시그널이 만들어집니다.
        # instance()메소드는 현재 인스턴스를 반환합니다.
        # 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메소드에 연결됩니다.
        # 이렇게 발신자(sender)와 수신자(receiver), 두 객체 간에 커뮤니케이션이 이루어집니다.
        # 이 예제에서 발신자는 푸시버튼(btn)이고, 수신자는 어플리케이션 객체(app)입니다.
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 툴팁은 어떤 위젯의 기능을 설명하는 등의 역할을 하는 말풍선 형태의 도움말입니다.
        # 위젯에 있는 모든 구성요소에 대하여 툴팁이 나타나도록 할 수 있습니다.

        # 먼저 툴팁에 사용될 폰트를 설정합니다. 여기엣어는 10px 크기의 'SansSerif' 폰트를 사용합니다.
        # 툴팁을 만들기 위해서는 setToolTip() 메소드를 사용해서 표시될 텍스트를 입력합니다.
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>Qwidget</b> widget')

        # 푸시버튼을 하나 만들고, 이 버튼에도 툴팁을 달아줍니다.
        btn1 = QPushButton('Button', self)
        btn1.setToolTip('This is a <b>QPushButton</b> widget')
        btn1.move(100, 100)
        # sizeHint() 메소드는 버튼을 적절한 크기로 설정하도록 도와줍니다.
        btn1.resize(btn1.sizeHint())

        self.show()

# __name__ 은 현재 모듈의 이름이 저장되는 내장 변수입니다.
# 만약 moduleA.py 라는 코드를 import 해서 예제 코드를 수행하면, __name__은 'moduleA'가 됩니다.
# 그렇지 않고 코드를 직접 실행한다면 __name__은 __main__ 이 됩니다. 따라서 이 한줄의 코드를 통해 프로그램이 직접 실행되는지
# 혹은 모듈을 통해 실행되는지를 확인합니다.


print(__name__)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
