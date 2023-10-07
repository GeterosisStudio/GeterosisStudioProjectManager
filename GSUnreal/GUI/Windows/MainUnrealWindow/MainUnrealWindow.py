import sys

from PySide6 import QtWidgets, QtUiTools

WINDOW_NAME = 'GSPM Jobs'
UI_FILE_FULLNAME = __file__.replace('.py', '.ui')

class MainUnrealWindow(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(MainUnrealWindow, self).__init__(parent)
		self.aboutToClose = None # This is used to stop the tick when the window is closed
		self.widget = QtUiTools.QUiLoader().load(UI_FILE_FULLNAME)
		self.widget.setParent(self)
		self.setWindowTitle(WINDOW_NAME)
		self.setGeometry(100, 100, self.widget.width(), self.widget.height())
		self.load()

	def closeEvent(self, event):
		if self.aboutToClose:
			self.aboutToClose(self)
		event.accept()


	def load(self):
		pass
