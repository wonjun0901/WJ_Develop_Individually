'''
QComboBox는 작은 공간을 차지하면서, 여러 옵션들을 제공하고 
그 중 하나의 옵션을 선택할 수 있도록 해주는 위젯입니다. (QComboBox 공식 문서 참고)
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        # QComboBox 위젯을 하나 만들고, addItem() 메서드를 이용해서 선택 가능한 4개의 옵션들을 추가했습니다.
        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        # 옵션을 선택하면, onActivated() 메서드가 호출됩니다.
        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# 하나의 라벨과 콤보 박스 위젯을 만들고 콤보박스에서 선택한 항목이 라벨에 나타나도록 했습니다.
