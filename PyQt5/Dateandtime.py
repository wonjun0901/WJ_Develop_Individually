from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QDate, Qt, QTime, QDateTime
# QDateTime 클래스를 사용해서 현재 날짜와 시간을 함께 출력할 수 있습니다.


# QDate 클래스는 날짜와 관련된 기능을 제공합니다.
# 우선 QDate 클래스를 이용해서 날짜를 출력해 보겠습니다.
# currentDate() 메소드는 현재 날짜를 반환합니다.
now = QDate.currentDate()
# toString() 메소드를 통해 현재 날짜를 문자열로 출력할 수 있습니다.
print(now.toString())
print(now.toString('d.M.yy'))  # 2.1.19
print(now.toString('dd.MM.yyyy'))  # 02.01.2019
print(now.toString('ddd.MMMM.yyyy'))  # 수.1월.2019
print(now.toString(Qt.ISODate))  # 2019-01-02
print(now.toString(Qt.DefaultLocaleLongDate))  # 2019년 1월 2일 수요일

time = QTime.currentTime()
print(time.toString())  # 15:41:22
print(time.toString('h.m.s'))  # 16.2.3
print(time.toString('hh.mm.ss'))  # 16.02.03
print(time.toString('hh.mm.ss.zzz'))  # 16.02.03.610
print(time.toString(Qt.DefaultLocaleLongDate))  # 오후 4:02:03
print(time.toString(Qt.DefaultLocaleShortDate))  # 오후 4:02


# currentDateTime() 메소드는 현재의 날짜와 시간을 반환합니다.
datetime = QDateTime.currentDateTime()
print(datetime.toString())


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
