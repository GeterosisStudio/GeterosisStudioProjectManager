import sys
import subprocess
import Settings
from PySide6 import QtWidgets
from PySide6 import QtUiTools
from PySide6.QtCore import Slot, Qt

from Plugins.GSMain import Log
from Settings import Settings
from Editor.GUI.Widgets.ProjectItem.ProjectItem import ProjectItem


class ProjectBrowserWindow(QtWidgets.QMainWindow):
    def __init__(self, main_path=None):
        super(ProjectBrowserWindow, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.ui.project_list_widget.setFocusPolicy(Qt.NoFocus)
        self.setWindowTitle('GSPM Project browser')
        self.setCentralWidget(self.ui)
        self.project_item_list = []
        self.main_path = main_path
        self.load()

    def load(self):
        self.update_project_list_widget()
        self.ui.project_list_widget.itemDoubleClicked.connect(self.item_double_click)
        self.load_window_config()

    def get_project_item_list(self):
        return self.project_item_list

    def get_project_dict(self):
        return Settings.load_projects()

    def create_project_item(self, item_dict):
        proj_path = item_dict["prod_path"]
        item = QtWidgets.QListWidgetItem()
        project_item = ProjectItem(proj_path)
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
        self.open_proj(self.ui.project_list_widget.itemWidget(item).project_path)

    def open_proj(self, proj_path):
        # TODO fix dont opened project from execute this file
        if proj_path:
            subprocess.Popen([sys.executable, self.main_path, proj_path])
            self.close()
        else:
            Log.warning("Project file not found.")


    def load_window_config(self):
        config = Settings.get_config()
        self.resize(config["Project browser"]["weight"], config["Project browser"]["height"])
        self.move(config["Project browser"]["horizontal"], config["Project browser"]["vertical"])

    def closeEvent(self, event):
        config = Settings.get_config()
        config["Project browser"]["weight"] = self.size().width()
        config["Project browser"]["height"] = self.size().height()
        config["Project browser"]["horizontal"] = self.pos().x()
        config["Project browser"]["vertical"] = self.pos().y()
        Settings.save_config(config)

        event.accept()

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import main
    app = QApplication()
    window = ProjectBrowserWindow(main.__file__.replace("\\", "/"))
    window.show()
    sys.exit(app.exec())
