from PySide6 import QtUiTools
from PySide6.QtWidgets import QMainWindow


class MainUnrealWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainUnrealWindow, self).__init__(parent)
        self.aboutToClose = None  # This is used to stop the tick when the window is closed
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.setWindowTitle('GSPM Jobs')
        self.setCentralWidget(self.ui)
        self.load()

    def closeEvent(self, event):
        if self.aboutToClose:
            self.aboutToClose(self)
        event.accept()

    def load(self):
        pass


"""
import GSUnreal.GUI.Windows.MainUnrealWindow.MainUnrealWindow as MainUnrealWindow
from GSUnreal.GUI.Windows import UnrealMixin
UnrealMixin.spawnQtWindow(MainUnrealWindow.MainUnrealWindow)
"""