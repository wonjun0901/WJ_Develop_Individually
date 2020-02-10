''' 가장 일반적인 레이아웃 클래스는 '그리드 레이아웃(grid layout)'입니다.
이 레이아웃 클래스는 위젯의 공간을 행(row)과 열(column)로 구분합니다.
그리드 레이아웃을 생성하기 위해 QGridLayout 클래스를 사용합니다.

위 예시 다이얼로그의 경우, 세 개의 행(Row)과 다섯 개의 열(Column)로 구분되어 있고, 필요한 위치에 위젯을 배치했습니다.
'''
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # QGridLayout을 만들고, 어플리케이션 창의 레이아웃으로 설정합니다.
        grid = QGridLayout()
        self.setLayout(grid)

        # addWidget() 메서드의 첫 번째 위젯은 추가할 위젯,
        # 두, 세 번째 위젯은 각각 행과 열 번호를 입력합니다.
        # 세 개의 라벨을 첫 번째 열에 수직으로 배치합니다.

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
