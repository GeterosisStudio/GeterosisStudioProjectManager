import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from GSMain.Editor.GUI.Windows.Project.ProjectWindow import ProjectWindow
from GSMain.Editor.GUI.Windows.ProjectBrowser.ProjectBrowserWindow import ProjectBrowserWindow
from Core import Icons


app = QApplication()
if len(sys.argv) > 1:
    window = ProjectWindow(sys.argv[1])
else:
    window = ProjectBrowserWindow(__file__.replace("\\", "/"))


app.setWindowIcon(QIcon(Icons.get_icon_path_from_name("GSPM.ico")))
window.show()
sys.exit(app.exec())
