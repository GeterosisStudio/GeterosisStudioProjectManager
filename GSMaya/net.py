from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile('E:/Projects/core/GeterozisProjectManager/GeterosisProjectManager/GSMaya/GUI/Windows/AnimationScene/AnimScene2.ui')
        file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.ui.button)
        self.setLayout(layout)

        self.ui.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("YES")

my_window = MyWindow()
my_window.show()