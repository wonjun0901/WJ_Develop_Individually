from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from open_file import *


class WidgetinMainwindow1(QWidget):
    def __init__(self):
        super().__init__()
        labels = QLabel("wow")
        labels.resize(100, 100)
        #labels.setGeometry(100, 100, 100, 200)
        labels.setAlignment(Qt.AlignCenter)
        line_edit = QLineEdit()
        btn1 = QPushButton('first button')
        btn2 = QPushButton('second button')
        #fileopen = fileoptions()

        btn1.clicked.connect(fileoptions.openFileNameDialog)
        btn2.clicked.connect(fileoptions.openFileNamesDialog)

        layout_btn = QHBoxLayout()
        layout_btn.addWidget(btn1)
        layout_btn.addWidget(btn2)

        layout_whole = QVBoxLayout()
        layout_whole.addWidget(labels)
        layout_whole.addWidget(line_edit)
        layout_whole.addLayout(layout_btn)

        self.setLayout(layout_whole)
