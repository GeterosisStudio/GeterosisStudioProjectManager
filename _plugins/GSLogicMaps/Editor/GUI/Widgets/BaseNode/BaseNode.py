import sys
import os
import json
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QWidget, QMenu
from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
from PySide6.QtGui import QIcon
from Core import Icons
from Service.Network import Client

class BaseNode(QWidget):
    def __init__(self):
        super(BaseNode, self).__init__()
        self.setWindowTitle('pass')
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)




if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication()
    window = BaseNode()
    window.show()
    sys.exit(app.exec())