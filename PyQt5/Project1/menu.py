import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from open_file import *


class menubar_main(QMenuBar):

    def __init__(self):
        super().__init__()

        file_menu = self.addMenu('&File')
        edit_menu = self.addMenu('&Edit')

        openAction = QAction('Open the file', file_menu)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open the file')
        openAction.triggered.connect(fileoptions.openFileNameDialog)

        open_many_Action = QAction('Open several files', file_menu)
        open_many_Action.setShortcut('Ctrl+O+S')
        open_many_Action.setStatusTip('Open several files')
        open_many_Action.triggered.connect(fileoptions.openFileNamesDialog)

        exitAction = QAction('Exit', file_menu)
        exitAction.setShortcut('Ctrl+q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction('Save', file_menu)
        saveAction.setShortcut('Ctrl+s')
        saveAction.setStatusTip('Save application')
        # openAction.triggered.connect(qApp.quit)

        # add Actions
        file_menu.addAction(openAction)
        file_menu.addAction(open_many_Action)
        file_menu.addAction(saveAction)
        file_menu.addSeparator()
        file_menu.addAction(exitAction)
