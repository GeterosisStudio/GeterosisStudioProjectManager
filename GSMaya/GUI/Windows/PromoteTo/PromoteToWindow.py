from PySide2 import QtWidgets, QtUiTools


class PromoteToWindow(QtWidgets.QWidget):
    def __init__(self):
        super(PromoteToWindow, self).__init__()

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(
            'E:/Projects/core/GeterozisProjectManager/GeterosisProjectManager/GSMaya/GUI/Windows/PromoteTo/PromoteTo.ui')
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

    def load(self):
        self.ui.show()

    def on_button_clicked(self):
        print("YES")