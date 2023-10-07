import sys

from PySide6 import QtWidgets, QtUiTools

WINDOW_NAME = 'GSPM Jobs'
UI_FILE_FULLNAME = __file__.replace('.py', '.ui')


class JobManager(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(JobManager, self).__init__(parent)
        self.aboutToClose = None  # This is used to stop the tick when the window is closed
        self.ui = QtUiTools.QUiLoader().load(UI_FILE_FULLNAME)
        self.ui.setParent(self)
        self.setWindowTitle(WINDOW_NAME)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)
        self.load()

    def closeEvent(self, event):
        if self.aboutToClose:
            self.aboutToClose(self)
        event.accept()

    def load(self):
        pass

"""
import GSUnreal.GUI.Windows.JobManager.JobManager as JobManager
from GSUnreal.GUI.Windows import UnrealMixin
UnrealMixin.spawnQtWindow(JobManager.JobManager)
"""