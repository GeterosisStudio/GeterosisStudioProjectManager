import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from GSMain.Editor.GUI.Windows.Project.Project import Project
from GSMain.Editor.GUI.Windows.ProjectBrowser.ProjectBrowser import ProjectBrowser
from Core import Icons


app = QApplication()
if len(sys.argv) >= 2:
    window = Project(sys.argv[1])
else:
    window = ProjectBrowser(__file__.replace("\\", "/"))


app.setWindowIcon(QIcon(Icons.get_icon_path_from_name("GSPM.ico")))
window.show()
sys.exit(app.exec())
