from PySide6 import QtWidgets, QtUiTools
from PySide6.QtWidgets import QApplication
import sys


class AssetItem(QtWidgets.QWidget):
    def __init__(self, item_data=None):
        super(AssetItem, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.ui)
        self.colors = {
            "PURPLE": '#ed7eed',
            "INDIGO": '#1fb0ff',
            "BLUE": '#00e5e5',
            "GREEN": '#344A1C',
            "GREEN WHITE": '#4E9500',
            "YELLOW": '#C3A300',
            "RED": '#750100',
            "RED WHITE": '#BB1715',
            "GREY": '#464646',
            "GREY WHITE": '#757575',
            "WHITE": '#ffffff'
        }

        self.item_status = self.colors["GREEN"]
        self.is_input = True
        self.is_output = True
        self.is_user = True

        if self.is_input:
            self.input_status = self.colors["GREEN WHITE"]
            self.set_input_status(self.colors["GREEN WHITE"])
        else:
            self.ui.input.deleteLater()

        if self.is_output:
            self.output_status = self.colors["GREEN WHITE"]
            self.set_output_status(self.colors["GREEN WHITE"])
        else:
            self.ui.output.deleteLater()

        if self.is_user:
            self.uset_status = self.colors["WHITE"]
            self.set_user_status(self.colors["GREY WHITE"])
        else:
            self.ui.user.deleteLater()

        self.set_item_status(self.colors["GREEN"])

    def set_input_status(self, status):
        if not status in list(self.colors.values()) or not self.is_input:
            return False
        self.input_status = status
        style = "QFrame{background-color: " + self.input_status + "; border: 1px solid #000000; border-radius: 4px;}"
        self.ui.input.setStyleSheet(style)

    def set_output_status(self, status):
        if not status in list(self.colors.values()) or not self.is_output:
            return False
        self.output_status = status
        style = "QFrame{\nbackground-color: " + self.output_status + ";\nborder: 1px solid #000000;\nborder-radius: 4px;\n}"
        self.ui.output.setStyleSheet(style)

    def set_user_status(self, status):
        if not status in list(self.colors.values()) or not self.is_user:
            return False
        self.uset_status = status
        style = "QFrame{\nbackground-color: " + self.uset_status + ";\nborder: 1px solid #000000;\nborder-radius: 15px;\n}"
        self.ui.user.setStyleSheet(style)

    def set_item_status(self, status):
        if not status in list(self.colors.values()):
            return False
        style = "QFrame{background-color:" + status + ";border: 1px solid #000000;border-radius: 4px;}"
        self.ui.item.setStyleSheet(style)


if __name__ == "__main__":
    app = QApplication()
    window = AssetItem()
    window.show()
    sys.exit(app.exec())
