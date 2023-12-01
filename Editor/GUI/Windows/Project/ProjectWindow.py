import sys
import json
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtUiTools


class ProjectWindow(QMainWindow):
    def __init__(self, PROJECT = None):
        super(ProjectWindow, self).__init__()
        self.project_info = self.load(PROJECT)
        self.setWindowTitle('GSPM Editor: ' + self.project_info["name"])
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.setCentralWidget(self.ui)

    def load(self, projrct_file):
        with open(projrct_file) as f:
            return json.load(f)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    window = ProjectWindow("E:/Projects/ILLUSION_1/ILLUSION_1.gsproj")
    window.show()
    sys.exit(app.exec())
