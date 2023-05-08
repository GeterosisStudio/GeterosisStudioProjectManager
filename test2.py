from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout
from PyQt5.QtCore import QSize

class CustomWidget(QWidget):
    def __init__(self):
        super(CustomWidget, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        for i in range(5):
            button = QPushButton('Button {}'.format(i+1))
            button.setMinimumHeight(30)
            layout.addWidget(button)
        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        list_widget = QListWidget(self)
        list_widget.sizeHintForRow(80)
        for i in range(10):
            item = QListWidgetItem()
            custom_widget = CustomWidget()
            list_widget.addItem(item)
            list_widget.setItemWidget(item, custom_widget)

        self.setGeometry(500, 500, 600, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
