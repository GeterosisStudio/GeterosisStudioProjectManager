import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel, QComboBox
from PySide6.QtCore import Qt


class FileTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["File Name", "Size", "Date Modified"])
        self.setSortingEnabled(True)

        # Установка выбора целых строк
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)

        # Скрытие линий между элементами таблицы
        self.setShowGrid(False)

        # Установка темной темы с белыми буквами
        self.setStyleSheet("QTableWidget { background-color: #333; color: white; }")

        # Добавление данных в таблицу (замените этот код на свою логику получения файлов и их атрибутов)
        self.setRowCount(4)
        self.setItem(0, 0, QTableWidgetItem("file1.txt"))
        self.setItem(0, 1, QTableWidgetItem("100 KB"))
        self.setItem(0, 2, QTableWidgetItem("01/01/2022"))
        self.setItem(1, 0, QTableWidgetItem("file2.jpg"))
        self.setItem(1, 1, QTableWidgetItem("200 KB"))
        self.setItem(1, 2, QTableWidgetItem("02/01/2022"))
        self.setItem(2, 0, QTableWidgetItem("file3.doc"))
        self.setItem(2, 1, QTableWidgetItem("50 KB"))
        self.setItem(2, 2, QTableWidgetItem("03/01/2022"))
        self.setItem(3, 0, QTableWidgetItem("file4.pdf"))
        self.setItem(3, 1, QTableWidgetItem("300 KB"))
        self.setItem(3, 2, QTableWidgetItem("04/01/2022"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        file_table_widget = FileTableWidget()

        # Добавление выпадающего списка для выбора сортировки


        # Размещение виджетов в главном окне
        layout = QVBoxLayout()
        layout.addWidget(file_table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())