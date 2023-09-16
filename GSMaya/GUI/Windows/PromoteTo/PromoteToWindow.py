from PySide2 import QtWidgets, QtUiTools
import os

class PromoteToWindow(QtWidgets.QWidget):
    def __init__(self):
        super(PromoteToWindow, self).__init__()

        loader = QtUiTools.QUiLoader()
        relative_file_path = "/GSMaya/GUI/Windows/PromoteTo/PromoteTo.ui"
        ui_path = os.getcwd() + relative_file_path
        self.ui = loader.load(ui_path)
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

    def load(self):
        self.ui.show()

    def on_button_clicked(self):
        print("YES")