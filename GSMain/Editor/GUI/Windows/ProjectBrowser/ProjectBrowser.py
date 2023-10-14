import sys
import subprocess

from PySide6 import QtWidgets
from PySide6 import QtUiTools
from PySide6.QtCore import Slot

from Settings import Settings
from GSMain.Editor.GUI.WIdgets.ProjectItem.ProjectItem import ProjectItem


class ProjectBrowser(QtWidgets.QMainWindow):
    def __init__(self, main_path=None):
        super(ProjectBrowser, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.setWindowTitle('GSPM Project browser')
        self.setCentralWidget(self.ui)
        self.project_item_list = []
        self.setGeometry(100, 60, 1000, 800)
        self.main_path = main_path
        self.load()

    def load(self):
        self.update_project_list_widget()
        self.ui.project_list_widget.itemDoubleClicked.connect(self.item_double_click)


    def get_project_item_list(self):
        return self.project_item_list

    def get_project_dict(self):
        return Settings.load_projects()

    def create_project_item(self, item_dict):
        proj_path = item_dict["prod_path"]
        item = QtWidgets.QListWidgetItem()
        project_item = ProjectItem(proj_path)
        item.setData(1, proj_path)
        item.setSizeHint(project_item.sizeHint())
        self.ui.project_list_widget.addItem(item)
        self.ui.project_list_widget.setItemWidget(item, project_item)

    def update_project_list_widget(self):
        self.ui.project_list_widget.clear()

        projects_dict = self.get_project_dict()
        for key in projects_dict:
            self.create_project_item(projects_dict[key])

    @Slot()
    def item_double_click(self, item):
        self.open_proj(item.data(1))

    def open_proj(self, proj_path):
        subprocess.Popen([sys.executable, self.main_path, proj_path])
        self.close()