from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from open_file import *
from makingheatmap import*


class WidgetinMainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uiforfirstwidget()

    def uiforfirstwidget(self):
        self.labels = QLabel("사랑해~ 여보양 이히히히히힝 ")
        self.labels.resize(100, 100)
        #labels.setGeometry(100, 100, 100, 200)
        self.labels.setAlignment(Qt.AlignCenter)
        line_edit = QLineEdit()
        btn1 = QPushButton('first button')
        btn2 = QPushButton('second button')
        btn3 = QPushButton('Make the heatmap')
        #fileopen = fileoptions()

        line_edit.textChanged[str].connect(self.showinglineedit)
        #heatmaps = heatmap_figure()
        #heatmaps1 = heatmaps.setupUI()

        layout_btn = QHBoxLayout()
        layout_btn.addWidget(btn1)
        layout_btn.addWidget(btn2)
        layout_btn.addWidget(btn3)

        layout_whole = QVBoxLayout()
        layout_whole.addWidget(self.labels)
        layout_whole.addWidget(line_edit)
        layout_whole.addLayout(layout_btn)

        self.setLayout(layout_whole)

        btn1.clicked.connect(self.openfile_widget)
        btn2.clicked.connect(self.open_severalfiles_widget)
        btn3.clicked.connect(self.showingheatmap_widget)

    # <===
    def openfile_widget(self):
        self.openfile = fileoptions()
        self.openfile.openFileNameDialog()

    def open_severalfiles_widget(self):
        self.sevopenfiles = fileoptions()
        self.sevopenfiles.openFileNamesDialog()

    def showingheatmap_widget(self):
        self.heatmaps = heatmap_figure()
        self.heatmaps.show()
        # self.hide()

    def showinglineedit(self, text):

        self.labels.setText(text)
