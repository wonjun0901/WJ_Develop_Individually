import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

iconroot = os.path.dirname(__file__)
ORGANIZATION_NAME = 'Circular App'
ORGANIZATION_DOMAIN = 'Circular shape'
APPLICATION_NAME = 'Circulargeometry program'
SETTINGS_TRAY = 'settings/tray'

QSS = """
QTreeWidget{
    border:none;
 } 

QTreeView::branch:has-siblings:!adjoins-item {
   border-image: url(images/vline.png) 0;
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(images/branch-more.png) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(images/branch-end.png) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    border-image: none;
    image: url(images/branch-closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
    border-image: none;
    image: url(images/branch-open.png);
}
"""



class TreeWidget(QtWidgets.QTreeWidget):
    currentTextChanged = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(TreeWidget, self).__init__(parent)
        self.currentItemChanged.connect(self.onCurrentItemChanged)
        self.setHeaderLabel('Standard Section Library')
        self.setRootIsDecorated(True)
        self.setAlternatingRowColors(True)
        self.readSettings()
        self.expandAll()

    def onCurrentItemChanged(self, current, previous):
        if current not in [self.topLevelItem(ix) for ix in range(self.topLevelItemCount())]:
            self.currentTextChanged.emit(current.text(0))

    def readSettings(self):
        settings = QtCore.QSettings()
        settings.beginGroup("TreeWidget")
        values = settings.value("items")
        if values is None:
            self.loadDefault()
        else:
            TreeWidget.dataToChild(values, self.invisibleRootItem())
            self.customized_item = None
            for ix in range(self.topLevelItemCount()):
                tlevel_item = self.topLevelItem(ix)
                if tlevel_item.text(0) == "Customized":
                    self.customized_item = tlevel_item
        settings.endGroup()

    def writeSettings(self):
        settings = QtCore.QSettings()
        settings.beginGroup("TreeWidget")
        settings.setValue("items", TreeWidget.dataFromChild(self.invisibleRootItem()))
        settings.endGroup()

    def loadDefault(self):
        standardsectionlist = ["D100","D150","D200","D250","D300","D350","D400","D450","D500",
        "D550","D600","D650","D700","D750","D800","D850","D900","D950","D1000"]
        rootItem = QtWidgets.QTreeWidgetItem(self, ['Circular shapes'])
        rootItem.setIcon(0, QtGui.QIcon(os.path.join(iconroot,"images/circularcolumnnorebar.png")))
        for element in standardsectionlist:
            rootItem.addChild(QtWidgets.QTreeWidgetItem([element]))

        self.customized_item = QtWidgets.QTreeWidgetItem(self, ["Customized"])
        self.customized_item.setIcon(0, QtGui.QIcon(os.path.join(iconroot,"images/circularcolumnnorebar.png")))

    @staticmethod
    def dataToChild(info, item):
        TreeWidget.tupleToItem(info["data"], item)
        for val in info["childrens"]:
            child = QtWidgets.QTreeWidgetItem()
            item.addChild(child)
            TreeWidget.dataToChild(val, child)

    @staticmethod
    def tupleToItem(t, item):
        # set values to item
        ba, isSelected = t
        ds = QtCore.QDataStream(ba)
        ds >> item
        item.setSelected(isSelected) 

    @staticmethod
    def dataFromChild(item):
        l = []
        for i in range(item.childCount()):
            child = item.child(i)
            l.append(TreeWidget.dataFromChild(child))
        return {"childrens": l, "data": TreeWidget.itemToTuple(item)}

    @staticmethod
    def itemToTuple(item):
        # return values from item
        ba = QtCore.QByteArray()
        ds = QtCore.QDataStream(ba, QtCore.QIODevice.WriteOnly)
        ds << item
        return ba, item.isSelected()


class InfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(InfoWidget, self).__init__(parent)
        hlay = QtWidgets.QHBoxLayout(self)
        plabel = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(os.path.join(iconroot, "images/circularcolumnnorebard.png"))\
                    .scaled(230, 230, QtCore.Qt.KeepAspectRatio)
        plabel.setPixmap(pixmap)
        hlay.addWidget(plabel)
        self.ilabel = QtWidgets.QLabel()
        hlay.addWidget(self.ilabel)
        hlay.addStretch()
        self.readSettings()

    @QtCore.pyqtSlot(str)
    def setData(self, text):
        try:
            circular_section = int(text.translate({ord('D'): ""}))
            area = (3.1416/4)*(circular_section**2)
            inertia = (3.1416/64)*circular_section**4
            fmt = "D = {}mm\nA = {:0.2E}mm2\n I  = {:0.2E}mm4"
            self.ilabel.setText(fmt.format(circular_section, area, inertia))
        except ValueError:
            pass
        return print(circular_section)
    def readSettings(self):
        settings = QtCore.QSettings()
        settings.beginGroup("InfoWidget")
        self.ilabel.setText(settings.value("text", ""))
        settings.endGroup()

    def writeSettings(self):
        settings = QtCore.QSettings()
        settings.beginGroup("InfoWidget")
        settings.setValue("text", self.ilabel.text())
        settings.endGroup()


class CircularDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CircularDialog, self).__init__(parent)

        self.setWindowTitle("Frequently used shape")
        self.setWindowIcon(QtGui.QIcon(os.path.join(iconroot+"/images/circularcolumnnorebar.png")))


        grid = QtWidgets.QGridLayout(self)

        self.tree = TreeWidget()
        self.infoWidget = InfoWidget()

        section_lay = QtWidgets.QHBoxLayout()
        section_label = QtWidgets.QLabel("Section name: ")
        self.section_edit = QtWidgets.QLineEdit('Define en name to section')
        section_lay.addWidget(section_label)
        section_lay.addWidget(self.section_edit)

        self.tree.currentTextChanged.connect(self.infoWidget.setData)

        button_layout = QtWidgets.QVBoxLayout()
        add_button = QtWidgets.QPushButton("Add")
        add_button.clicked.connect(self.addItem)
        delete_button = QtWidgets.QPushButton("Delete")
        delete_button.clicked.connect(self.removeItem)
        button_layout.addWidget(add_button, alignment=QtCore.Qt.AlignBottom)
        button_layout.addWidget(delete_button, alignment=QtCore.Qt.AlignTop)

        buttonBox = QtWidgets.QDialogButtonBox()
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept) 
        buttonBox.rejected.connect(self.reject)
        self.accepted.connect(self.save_all_data)
        self.rejected.connect(self.save_all_data)

        grid.addLayout(section_lay, 0, 0)
        grid.addWidget(self.tree, 1, 0)
        grid.addLayout(button_layout, 1, 1)
        grid.addWidget(self.infoWidget, 2, 0, 1, 2)
        grid.addWidget(buttonBox, 3, 0, 1, 2)
        self.readSettings()

    def readSettings(self):
        settings = QtCore.QSettings()
        settings.beginGroup("CircularDialog")
        self.setGeometry(settings.value("geometry", QtCore.QRect(300, 300, 400, 600)))
        self.section_edit.setText(settings.value("SectionInfo", "Define en name to section"))
        settings.endGroup()

    def writeSettings(self):
        settings = QtCore.QSettings()
        settings.beginGroup("CircularDialog")
        settings.setValue("geometry", self.geometry())
        settings.setValue("SectionInfo",self.section_edit.text())
        settings.endGroup()

    def closeEvent(self, event):
        self.save_all_data()
        super(CircularDialog, self).closeEvent(event)

    def save_all_data(self):
        for children in self.findChildren(QtWidgets.QWidget) + [self]:
            if hasattr(children, "writeSettings"):
                children.writeSettings()

    def addItem(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "Add custom section", 
            "Enter section geometry f.ex as D325 or just 325 in mm: ")
        if ok:
            it = QtWidgets.QTreeWidgetItem([text])
            self.tree.customized_item.addChild(it)

    def removeItem(self):
        it = self.tree.customized_item.takeChild(0)
        del it


if __name__ == '__main__':
    QtCore.QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QtCore.QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QtCore.QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(QSS)
    w = CircularDialog()
    w.show()
    sys.exit(app.exec_())