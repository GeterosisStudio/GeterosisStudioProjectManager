import sys
from PySide6 import QtWidgets
from PySide6 import QtUiTools
from Settings import Settings

class ProjectBrowser(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProjectBrowser, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.setWindowTitle('GSPM Project browser')
        self.setCentralWidget(self.ui)
        self.project_item_list = []
        self.setGeometry(100, 60, 1000, 800)
        self.load()

    def load(self):
        self.update_project_list_widget()

    def get_project_item_list(self):
        return self.project_item_list

    def get_project_dict(self):
        return Settings.load_projects()

    def add_project_item(self, item):
        self.ui.project_list_widget.addItem(item)

    def create_project_item(self, item_dict):
        name = item_dict["name"]
        proj_path = item_dict["prod_path"]
        item_text = name + "    " + proj_path
        return QtWidgets.QListWidgetItem(item_text)

    def update_project_list_widget(self):
        self.ui.project_list_widget.clear()

        projects_dict = self.get_project_dict()
        for key in projects_dict:
            self.add_project_item(self.create_project_item(projects_dict[key]))


