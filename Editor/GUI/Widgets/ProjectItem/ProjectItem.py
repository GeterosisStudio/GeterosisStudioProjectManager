import os
import json
from PySide6 import QtWidgets, QtUiTools
from PySide6.QtGui import QIcon


class ProjectItem(QtWidgets.QWidget):

    def __init__(self, project_path=None):
        super(ProjectItem, self).__init__()
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(__file__.replace('.py', '.ui'))
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)

        self.proj_ext = '.gsproj'
        self.project_path = self.set_project_path(project_path)
        self.project_file = self.set_project_file()
        self.project_info = self.load_project_info()
        self.load()

    def set_project_path(self, project_path):
        project_path = project_path.replace("\\", "/")

        if os.path.isdir(project_path):
            for elem in os.listdir(project_path):
                if os.path.isfile(os.path.join(project_path, elem)):
                    if os.path.splitext(os.path.join(project_path, elem))[1] == self.proj_ext:
                        if project_path[-1] != "/":
                            project_path += "/"
                        return project_path

        if os.path.isfile(project_path):
            if os.path.splitext(project_path)[1] == self.proj_ext:
                return project_path.replace(project_path.split("/")[-1], "")
        return False

    def set_project_file(self):
        if not self.project_path: return False
        for elem in os.listdir(self.project_path):
            if elem[-7:] == self.proj_ext:
                return elem
        return False

    def load_project_info(self):
        if not self.project_file: return False
        with open(self.project_path + self.project_file, "r") as inf:
            info = json.load(inf)
        return info

    def load(self):
        if self.project_info: self.ui.project_name.setText(self.project_info["name"])
        if self.project_path and self.project_file: self.ui.project_path.setText(self.project_path + self.project_file)

        if self.project_info and self.project_info["image"]:
            self.ui.project_icon

            icon_label = QtWidgets.QLabel(self.ui.project_icon)
            icon = QIcon(self.project_path + self.project_info["image"])
            pixmap = icon.pixmap(60, 60)
            icon_label.setPixmap(pixmap)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    if len(sys.argv) >= 2:
        q = QApplication(sys.argv[1])
    else:
        q = QApplication()
    w = ProjectItem("E:/Projects/ILLUSION_1")
    w.show()
    sys.exit(q.exec())
