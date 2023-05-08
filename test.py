<<<<<<< HEAD
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('F:/bufer/untitled.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
=======
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget, QApplication

class FolderTree(QTreeWidget):
    def __init__(self, path):
        super(FolderTree, self).__init__()
        self.path = path
        self.setHeaderLabels(['Name'])
        self.dirdata = self.create_dir_data(self.path)
        self.create_tree_widget(self, self.dirdata)

    def create_tree_widget(self, parent, dir_data):
        for key, value in dir_data.items():
            item = QTreeWidgetItem(parent, [key])
            if isinstance(value, dict):
                self.create_tree_widget(item, value)
            elif isinstance(value, list):
                for item_value in value:
                    QTreeWidgetItem(item, [str(item_value)])
            else:
                QTreeWidgetItem(item, [str(value)])

    def create_dir_data(self,dir_path):
        return {
            'assets': [i for i in os.listdir(os.path.join(dir_path, 'assets')) if
                       os.path.isdir(os.path.join(dir_path, 'assets', i))],
            'animation': {

                'scenes': [i for i in os.listdir(os.path.join(dir_path, 'animation', 'scenes')) if
                           os.path.isdir(os.path.join(dir_path, 'animation', 'scenes', i))],
                'movement': [i for i in os.listdir(os.path.join(dir_path, 'animation', 'movement')) if
                             os.path.isdir(os.path.join(dir_path, 'animation', 'movement', i))],
            },
            'logicmaps': {

                'scenes': list(os.listdir(os.path.join(dir_path, 'logicmaps', 'scenes'))),
                'gameplay': list(os.listdir(os.path.join(dir_path, 'logicmaps', 'gameplay')))
            }
        }

    def openFolder(self, item, column):
        path = self.itemPath(item)
        print (path)
        if os.path.isdir(path):
            url = QUrl.fromLocalFile(path)
            QDesktopServices.openUrl(url)

    def show_subelems(self, item):
        item.setExpanded(True)

    def itemPath(self, item):
        path = [item.text(0)]
        while item.parent() is not None:
            item = item.parent()
            path.insert(0, item.text(0))
        return os.path.join(self.path, *path)


if __name__ == '__main__':
    app = QApplication([])
    tree = FolderTree("E:/Projects/ILLUSION_1")
    tree.itemDoubleClicked.connect(tree.openFolder)
    tree.itemClicked.connect(tree.show_subelems)
    tree.show()
    app.exec_()
>>>>>>> master
