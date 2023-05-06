import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget, QApplication

class FolderTree(QTreeWidget):
    def __init__(self, path):
        super(FolderTree, self).__init__()
        self.path = path
        self.setHeaderLabels(['Name'])
        self.populate()

    def populate(self):
        self.clear()
        for name in os.listdir(self.path):
            path = os.path.join(self.path, name)
            if os.path.isdir(path):
                item = QTreeWidgetItem([name, ''])
                self.addTopLevelItem(item)
                self.populate_folder(item, path)


    def populate_folder(self, parent, path):
        for name in os.listdir(path):
            child_path = os.path.join(path, name)
            if os.path.isdir(child_path):
                child_item = QTreeWidgetItem([name, ''])
                parent.addChild(child_item)
                self.populate_folder(child_item, child_path)

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
    tree = FolderTree(r"E:\Projects\ILLUSION_1\animation")
    tree.itemDoubleClicked.connect(tree.openFolder)
    tree.itemClicked.connect(tree.show_subelems)
    tree.show()
    app.exec_()
