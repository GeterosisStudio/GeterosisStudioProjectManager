from PyQt5 import QtWidgets, uic, QtCore
import os
import sys
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("")
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1.5"
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
