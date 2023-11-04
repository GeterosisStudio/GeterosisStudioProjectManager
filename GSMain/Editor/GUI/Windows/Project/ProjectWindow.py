import sys
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtUiTools


class ProjectWindow(QMainWindow):
    def __init__(self, PROJECT = None):
        super(ProjectWindow, self).__init__()
        self.setWindowTitle('GSPM Editor')
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.setCentralWidget(self.ui)
        self.load()

    def load(self):
        pass